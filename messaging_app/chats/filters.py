# messaging_app/chats/filters.py

import django_filters
from .models import Message  # Replace with your actual Message model
from django.contrib.auth.models import User  # Import User model for filtering

class MessageFilter(django_filters.FilterSet):
    user = django_filters.ModelChoiceFilter(queryset=User.objects.all(), field_name='sender')  # Filter by sender
    created_at = django_filters.DateTimeFromToRangeFilter(field_name='created_at')  # Filter by creation date range

    class Meta:
        model = Message
        fields = ['user', 'created_at']  # Add fields you want to filter by