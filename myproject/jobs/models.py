from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils import timezone


class CustomUser(AbstractUser):
    """
    Custom User model with company admin role
    """
    is_company_admin = models.BooleanField(default=False, help_text="Check if user is a company admin")
    company_name = models.CharField(max_length=255, blank=True, null=True, help_text="Company name (required for company admins)")

    def clean(self):
        """Validate that company_name is provided if user is company admin"""
        if self.is_company_admin and not self.company_name:
            raise ValidationError("Company name is required for company admins")

    def __str__(self):
        return f"{self.username} - {'Admin' if self.is_company_admin else 'User'}"


class Job(models.Model):
    """
    Job posting model
    """
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
    ]

    title = models.CharField(max_length=255, help_text="Job title")
    salary = models.DecimalField(max_digits=10, decimal_places=2, help_text="Annual salary")
    company_name = models.CharField(max_length=255, help_text="Company name")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open', help_text="Job status")
    description = models.TextField(help_text="Job description")
    years_of_experience = models.IntegerField(help_text="Required years of experience")
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='jobs', help_text="User who created this job")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Creation timestamp")
    updated_at = models.DateTimeField(auto_now=True, help_text="Last update timestamp")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} at {self.company_name}"


class JobApplication(models.Model):
    """
    Job application model - tracks when a user applies for a job
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='applications', help_text="User applying for job")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications', help_text="Job being applied for")
    applied_at = models.DateTimeField(auto_now_add=True, help_text="Application timestamp")

    class Meta:
        unique_together = ('user', 'job')
        ordering = ['-applied_at']

    def clean(self):
        """Validate that job is still open"""
        if self.job.status != 'open':
            raise ValidationError("Cannot apply to closed jobs")

    def __str__(self):
        return f"{self.user.username} applied for {self.job.title}"
