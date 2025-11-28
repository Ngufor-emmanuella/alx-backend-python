from django.db import models
from django.contrib.auth.models import User

class UnreadMessagesManager(models.Manager):
    def unread_for_user(self, user):
        # Filter unread messages for the specified user and optimize query
        return self.filter(receiver=user, read=False).only('id', 'content', 'timestamp', 'sender')

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    edited_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='edited_messages')
    parent_message = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    read = models.BooleanField(default=False)  # Indicates if the message has been read

    # Managers
    objects = models.Manager()  # Default manager
    unread_messages = UnreadMessagesManager()  # Custom manager for unread messages

    def __str__(self):
        return f'Message from {self.sender} to {self.receiver}: {self.content}'