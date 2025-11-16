#!/usr/bin/env python3

from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model."""
    
    class Meta:
        model = User
        fields = ('user_id', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'created_at')

class MessageSerializer(serializers.ModelSerializer):
    """Serializer for the Message model."""
    
    class Meta:
        model = Message
        fields = ('message_id', 'sender', 'conversation', 'message_body', 'sent_at')

class ConversationSerializer(serializers.ModelSerializer):
    """Serializer for the Conversation model."""
    messages = MessageSerializer(many=True, read_only=True, source='messages')

    class Meta:
        model = Conversation
        fields = ('conversation_id', 'participants', 'messages', 'created_at')