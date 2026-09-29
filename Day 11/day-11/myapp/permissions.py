from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):
    """Owner can edit/delete their own post. Admin (staff) can manage everything."""

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.owner == request.user