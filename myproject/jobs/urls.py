from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserRegistrationView, CustomTokenObtainPairView,
    JobViewSet, JobApplicationViewSet
)

# Create router for viewsets
router = DefaultRouter()
router.register(r'jobs', JobViewSet, basename='job')
router.register(r'applications', JobApplicationViewSet, basename='application')

app_name = 'jobs'

urlpatterns = [
    # Authentication endpoints
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),

    # Router URLs for viewsets
    path('', include(router.urls)),
]
