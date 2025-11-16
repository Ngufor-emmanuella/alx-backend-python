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
    sender = serializers.CharField(source='sender.email')  # Serialize sender as email

    class Meta:
        model = Message
        fields = ('message_id', 'sender', 'conversation', 'message_body', 'sent_at')

class ConversationSerializer(serializers.ModelSerializer):
    """Serializer for the Conversation model."""
    messages = MessageSerializer(many=True, read_only=True)  # Nested messages

    class Meta:
        model = Conversation
        fields = ('conversation_id', 'participants', 'messages', 'created_at')
    
    def create(self, validated_data):
        """Handle creation of a Conversation with nested Messages."""
        messages_data = validated_data.pop('messages', [])
        conversation = Conversation.objects.create(**validated_data)
        for message_data in messages_data:
            Message.objects.create(conversation=conversation, **message_data)
        return conversation

    def validate(self, data):
        """Validate data before creating a Conversation."""
        if not data.get('participants'):
            raise serializers.ValidationError("At least one participant is required.")
        return data