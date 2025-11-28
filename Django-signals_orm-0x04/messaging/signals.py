from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Message, MessageHistory

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_message = Message.objects.get(pk=instance.pk)
            if old_message.content != instance.content:  # Check if content is different
                MessageHistory.objects.create(message=old_message, old_content=old_message.content)
                instance.edited = True  # Set the edited flag to True
                instance.edited_by = instance.sender  # Capture the user making the edit
        except Message.DoesNotExist:
            pass  # If the message doesn't exist yet, do nothing