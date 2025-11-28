from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender} to {self.receiver}: {self.content}'
    

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User to notify
    message = models.ForeignKey(Message, on_delete=models.CASCADE)  # Linked message
    timestamp = models.DateTimeField(auto_now_add=True)  # Notification timestamp
    is_read = models.BooleanField(default=False)  # Read status of the notification

    def __str__(self):
        return f'Notification for {self.user}: {self.message.content}'