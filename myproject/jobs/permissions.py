from rest_framework import permissions


class IsCompanyAdmin(permissions.BasePermission):
    """
    Permission to check if user is a company admin
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_company_admin


class IsJobCreator(permissions.BasePermission):
    """
    Permission to check if user created the job
    """
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user


class IsRegularUser(permissions.BasePermission):
    """
    Permission to check if user is a regular user (not admin)
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and not request.user.is_company_admin
