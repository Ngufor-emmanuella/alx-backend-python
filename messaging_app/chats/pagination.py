# messaging_app/chats/pagination.py

from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 20  # Number of messages per page
    page_size_query_param = 'page_size'  # Allow clients to set a custom page size
    max_page_size = 100  # Limit for maximum page size