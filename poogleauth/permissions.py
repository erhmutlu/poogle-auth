from rest_framework.permissions import BasePermission

__author__ = 'erhmutlu'

class IsAdmin(BasePermission):
    """
    Allows access only to super users.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser