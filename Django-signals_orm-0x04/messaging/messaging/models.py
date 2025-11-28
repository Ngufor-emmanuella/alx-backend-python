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
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user to notify
    message = models.ForeignKey(Message, on_delete=models.CASCADE)  # The message linked to the notification
    timestamp = models.DateTimeField(auto_now_add=True)  # When the notification was created
    is_read = models.BooleanField(default=False)  # Whether the notification has been read

    def __str__(self):
        return f'Notification for {self.user}: {self.message.content}'

    