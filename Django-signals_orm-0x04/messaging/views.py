from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Message

@login_required
def inbox_view(request):
    # Fetch unread messages for the logged-in user using the custom manager
    unread_messages = (
        Message.unread_messages.unread_for_user(request.user)
        .select_related('sender')  # Optimize fetching of the sender information
        .order_by('timestamp')  # Order messages by timestamp
    )
    
    return render(request, 'messaging/inbox.html', {'unread_messages': unread_messages})