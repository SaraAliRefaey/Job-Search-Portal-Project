from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Job, JobApplication

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration
    """
    password = serializers.CharField(write_only=True, min_length=8)
    company_name = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_company_admin', 'company_name')

    def validate(self, data):
        """Validate that company_name is provided if user is company admin"""
        if data.get('is_company_admin') and not data.get('company_name'):
            raise serializers.ValidationError("Company name is required for company admins")
        return data

    def create(self, validated_data):
        """Create user with hashed password"""
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_company_admin=validated_data.get('is_company_admin', False),
            company_name=validated_data.get('company_name', '')
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user data
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_company_admin', 'company_name')
        read_only_fields = ('id',)


class JobSerializer(serializers.ModelSerializer):
    """
    Serializer for Job model
    """
    created_by = UserSerializer(read_only=True)
    application_count = serializers.SerializerMethodField()
    has_applied = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = (
            'id', 'title', 'salary', 'company_name', 'status',
            'description', 'years_of_experience', 'created_by',
            'created_at', 'updated_at', 'application_count', 'has_applied'
        )
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_at')

    def get_application_count(self, obj):
        """Get total number of applications for this job"""
        return obj.applications.count()

    def get_has_applied(self, obj):
        """Check if current user has applied for this job"""
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return JobApplication.objects.filter(
                user=request.user,
                job=obj
            ).exists()
        return False


class JobCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and updating jobs (company admins only)
    """
    class Meta:
        model = Job
        fields = (
            'title', 'salary', 'company_name', 'status',
            'description', 'years_of_experience'
        )

    def validate_status(self, value):
        """Validate status is either open or closed"""
        if value not in ['open', 'closed']:
            raise serializers.ValidationError("Status must be 'open' or 'closed'")
        return value

    def validate_years_of_experience(self, value):
        """Validate years of experience is non-negative"""
        if value < 0:
            raise serializers.ValidationError("Years of experience cannot be negative")
        return value


class JobApplicationSerializer(serializers.ModelSerializer):
    """
    Serializer for JobApplication model
    """
    job_detail = JobSerializer(source='job', read_only=True)
    user_detail = UserSerializer(source='user', read_only=True)

    class Meta:
        model = JobApplication
        fields = ('id', 'user', 'user_detail', 'job', 'job_detail', 'applied_at')
        read_only_fields = ('id', 'user', 'user_detail', 'applied_at')

    def validate(self, data):
        """Validate that job is still open"""
        job = data.get('job')
        if job and job.status != 'open':
            raise serializers.ValidationError("Cannot apply to closed jobs")
        return data


class JobApplicationListSerializer(serializers.ModelSerializer):
    """
    Simplified serializer for listing applications
    """
    job = JobSerializer(read_only=True)

    class Meta:
        model = JobApplication
        fields = ('id', 'job', 'applied_at')
        read_only_fields = ('id', 'applied_at')
