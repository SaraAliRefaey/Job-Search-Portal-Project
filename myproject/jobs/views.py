from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.core.exceptions import ValidationError

from .models import Job, JobApplication
from .serializers import (
    UserRegistrationSerializer, UserSerializer, JobSerializer,
    JobCreateUpdateSerializer, JobApplicationSerializer,
    JobApplicationListSerializer
)
from .permissions import IsCompanyAdmin, IsJobCreator, IsRegularUser

User = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom JWT token serializer with additional user data
    """
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['is_company_admin'] = user.is_company_admin
        return token


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom login view with additional user data
    """
    serializer_class = CustomTokenObtainPairSerializer


class UserRegistrationView(generics.CreateAPIView):
    """
    API view for user registration
    Allows anyone to register without authentication
    """
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


class JobViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Job model
    - list: Get all open jobs
    - create: Create job (company admin only)
    - retrieve: Get job details
    - update: Update job (owner only)
    - partial_update: Partial update job (owner only)
    - destroy: Delete job (owner only)
    - search: Search jobs by title or experience
    - admin_jobs: Get jobs created by authenticated admin
    """
    queryset = Job.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        """Use different serializers for different actions"""
        if self.action in ['create', 'update', 'partial_update']:
            return JobCreateUpdateSerializer
        return JobSerializer

    def get_queryset(self):
        """
        Filter queryset based on user type and action
        """
        if self.action == 'admin_jobs':
            # Only show jobs created by authenticated admin user
            return Job.objects.filter(created_by=self.request.user)
        elif self.action == 'list':
            # Regular users see only open jobs
            if not self.request.user.is_company_admin:
                return Job.objects.filter(status='open')
            # Admins see all jobs
            return Job.objects.all()
        else:
            # For other actions, return all jobs
            return Job.objects.all()

    def get_permissions(self):
        """
        Set permissions based on action
        """
        if self.action == 'create':
            permission_classes = [IsAuthenticated, IsCompanyAdmin]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsCompanyAdmin, IsJobCreator]
        elif self.action == 'admin_jobs':
            permission_classes = [IsAuthenticated, IsCompanyAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """Set the created_by field to current user"""
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        """Prevent changing the created_by field"""
        serializer.save(created_by=self.request.user)

    @action(detail=False, methods=['get'])
    def search(self, request):
        """
        Search jobs by title and years of experience
        Query parameters:
        - title: Job title (partial match)
        - experience: Years of experience (exact match)
        """
        queryset = self.get_queryset()

        # Search by title
        title = request.query_params.get('title', None)
        if title:
            queryset = queryset.filter(title__icontains=title)

        # Filter by years of experience
        experience = request.query_params.get('experience', None)
        if experience:
            try:
                experience = int(experience)
                queryset = queryset.filter(years_of_experience=experience)
            except ValueError:
                return Response(
                    {'error': 'Experience must be an integer'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def admin_jobs(self, request):
        """
        Get all jobs created by the authenticated company admin
        """
        if not request.user.is_company_admin:
            return Response(
                {'error': 'Only company admins can access this endpoint'},
                status=status.HTTP_403_FORBIDDEN
            )

        jobs = Job.objects.filter(created_by=request.user)
        serializer = self.get_serializer(jobs, many=True)
        return Response(serializer.data)


class JobApplicationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for JobApplication model
    - create: Apply for a job (regular users only)
    - list: List user's applications
    """
    serializer_class = JobApplicationListSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get', 'head', 'options']

    def get_queryset(self):
        """Only return applications for authenticated user"""
        return JobApplication.objects.filter(user=self.request.user)

    def get_permissions(self):
        """Set permissions based on action"""
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        """
        Apply for a job
        Request body: {"job": <job_id>}
        """
        job_id = request.data.get('job')

        if not job_id:
            return Response(
                {'error': 'Job ID is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            job = Job.objects.get(id=job_id)
        except Job.DoesNotExist:
            return Response(
                {'error': 'Job not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        # Check if job is open
        if job.status != 'open':
            return Response(
                {'error': 'Cannot apply to closed jobs'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if user already applied
        if JobApplication.objects.filter(user=request.user, job=job).exists():
            return Response(
                {'error': 'You have already applied for this job'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create application
        application = JobApplication.objects.create(user=request.user, job=job)
        serializer = self.get_serializer(application)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def my_applications(self, request):
        """Get all applications made by authenticated user"""
        applications = self.get_queryset()
        serializer = self.get_serializer(applications, many=True)
        return Response(serializer.data)

