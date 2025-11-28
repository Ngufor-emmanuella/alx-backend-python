from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Message

@login_required
def inbox_view(request):
    # Fetch unread messages for the logged-in user
    unread_messages = Message.unread_messages.for_user(request.user).order_by('timestamp')
    
    return render(request, 'messaging/inbox.html', {'unread_messages': unread_messages})