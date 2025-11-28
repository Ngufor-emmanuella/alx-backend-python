from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)  # New field to track edits

    def __str__(self):
        return f'Message from {self.sender} to {self.receiver}: {self.content}'
    

class MessageHistory(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='history')
    old_content = models.TextField()  # Stores the old content of the message
    edited_at = models.DateTimeField(auto_now_add=True)  # Time of the edit

    def __str__(self):
        return f'History for {self.message}: {self.old_content}'