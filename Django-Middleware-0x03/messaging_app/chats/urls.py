# messaging_app/chats/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet

router = DefaultRouter()
router.register(r'conversations/(?P<conversation_id>[^/.]+)/messages', MessageViewSet, basename='messages')

urlpatterns = [
    path('api/', include(router.urls)),
]