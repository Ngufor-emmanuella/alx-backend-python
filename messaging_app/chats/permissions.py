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
    

# messaging_app/chats/permissions.py

from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to only allow authenticated users who are participants
    in a conversation to send, view, update, and delete messages.
    """

    def has_permission(self, request, view):
        # Allow only authenticated users
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Check if the user is a participant in the conversation
        if not request.user.is_authenticated:
            return False

        # Check if the user is a participant in the conversation
        is_participant = obj.conversation.participants.filter(id=request.user.id).exists()

        # Allow GET requests and check for permission on unsafe methods
        if request.method in permissions.SAFE_METHODS:
            return True

        # For PUT, PATCH, DELETE, ensure the user is a participant
        return is_participant