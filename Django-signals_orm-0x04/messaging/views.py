from django.shortcuts import render, get_object_or_404
from .models import Message

def message_detail(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    history = message.history.all()  # Retrieve all historical edits
    return render(request, 'messaging/message_detail.html', {'message': message, 'history': history})

