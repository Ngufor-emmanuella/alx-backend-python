# messaging_app/chats/auth.py

# Example of custom authentication (optional)
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1] if 'HTTP_AUTHORIZATION' in request.META else None
        if not token:
            return None

        try:
            # Logic to validate token here, if needed
            pass
        except Exception:
            raise AuthenticationFailed('Invalid token')

        return (user, token)  # Return user and token