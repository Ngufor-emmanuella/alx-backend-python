# Django-Middleware-0x03/chats/middleware.py

from django.http import HttpResponseTooManyRequests
from django.utils import timezone
from collections import defaultdict
import time

class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.message_counts = defaultdict(list)  # Track message counts per IP

    def __call__(self, request):
        # Limit applies only to POST requests
        if request.method == 'POST' and request.path == '/api/conversations/send_message/':  # Adjust the path as needed
            ip_address = request.META.get('REMOTE_ADDR')
            current_time = timezone.now()

            # Clean up old timestamps for the past minute
            self.message_counts[ip_address] = [
                timestamp for timestamp in self.message_counts[ip_address]
                if (current_time - timestamp).total_seconds() < 60
            ]

            # Check if the user exceeds the message limit
            if len(self.message_counts[ip_address]) >= 5:
                return HttpResponseTooManyRequests("You have exceeded the message limit (5 messages per minute).")

            # Record the current timestamp for the new message
            self.message_counts[ip_address].append(current_time)

        # Call the next middleware or view
        response = self.get_response(request)
        return response