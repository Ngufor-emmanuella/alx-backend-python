# messaging_app/chats/permissions.py

from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsOwner(permissions.BasePermission):
   
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return obj.conversation.participants.filter(id=request.user.id).exists()

        # Check if the user is a participant in the conversation
        return obj.conversation.participants.filter(id=request.user.id).exists()
    
    def has_permission(self, request, view):
        # Allow access only for authenticated users
        return request.user and request.user.is_authenticated