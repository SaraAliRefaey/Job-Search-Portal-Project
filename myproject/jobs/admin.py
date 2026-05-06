from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Job, JobApplication


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Admin class for CustomUser model"""
    fieldsets = UserAdmin.fieldsets + (
        ('Company Information', {'fields': ('is_company_admin', 'company_name')}),
    )
    list_display = ('username', 'email', 'is_company_admin', 'company_name')
    list_filter = ('is_company_admin',) + UserAdmin.list_filter


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    """Admin class for Job model"""
    list_display = ('title', 'company_name', 'status', 'years_of_experience', 'salary', 'created_by', 'created_at')
    list_filter = ('status', 'created_at', 'years_of_experience')
    search_fields = ('title', 'company_name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    """Admin class for JobApplication model"""
    list_display = ('user', 'job', 'applied_at')
    list_filter = ('applied_at', 'job')
    search_fields = ('user__username', 'job__title')
    readonly_fields = ('applied_at',)
    ordering = ('-applied_at',)
