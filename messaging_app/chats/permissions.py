# messaging_app/chats/permissions.py

from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of a message to view or edit it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user  # Assuming obj has an 'owner' attribute