from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from .permissions import IsAuthenticatedAndParticipant


class ConversationViewSet(viewsets.ModelViewSet):
    """Viewset for handling conversations."""
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """Create a new conversation."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        conversation = serializer.save()  # Save and get the conversation instance
        
        # Handle participants
        participants = request.data.get('participants', [])
        conversation.participants.set(participants)  # Using set() to assign participants
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MessageViewSet(viewsets.ModelViewSet):
    """Viewset for handling messages."""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticatedAndParticipant] 
   
    def get_queryset(self):
        user = self.request.user
        conversation_id = self.kwargs.get('conversation_id')  # Assuming your URL has this parameter

        if conversation_id:
            return Message.objects.filter(conversation_id=conversation_id, conversation__participants=user)

        return Message.objects.none()  # Return an empty queryset if no conversation_id provided

    def create(self, request, *args, **kwargs):
        # Ensure the user is a participant before creating a message
        conversation_id = self.kwargs.get('conversation_id')
        conversation = self.get_object()  # Make sure to implement this method to get the conversation

        if conversation.participants.filter(id=request.user.id).exists():
            return super().create(request, *args, **kwargs)
        else:
            return Response({"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)