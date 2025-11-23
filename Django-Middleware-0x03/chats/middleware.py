# Django-Middleware-0x03/chats/middleware.py

from django.http import HttpResponseForbidden

class RolePermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user

        # Check if the user is authenticated
        if user.is_authenticated:
            # Check role
            if not (user.is_admin or user.is_moderator):
                return HttpResponseForbidden("You do not have permission to access this resource.")
        else:
            return HttpResponseForbidden("You must be logged in to access this resource.")

        # Call the next middleware or view
        response = self.get_response(request)
        return response