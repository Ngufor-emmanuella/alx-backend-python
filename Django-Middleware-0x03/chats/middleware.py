from django.http import HttpResponseForbidden
from datetime import datetime

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_time = datetime.now().hour  # Get the current hour

        # Restrict access outside of 9 PM and 6 AM
        if current_time < 21 and current_time >= 6:
            return HttpResponseForbidden("Access to the chat is restricted during this time.")

        # Call the next middleware or view if within allowed hours
        response = self.get_response(request)
        return response