# Django-Middleware-0x03/chats/middleware.py

import logging
from datetime import datetime

# Configure the logger
logging.basicConfig(
    filename='requests.log',
    level=logging.INFO,
    format='%(asctime)s %(message)s',
)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else 'Anonymous'
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"
        
        # Log the request information
        logging.info(log_message)

        # Call the next middleware or view
        response = self.get_response(request)
        return response