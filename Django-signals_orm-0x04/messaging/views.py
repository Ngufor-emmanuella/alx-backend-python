from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Message
from django.views.decorators.cache import cache_page


@login_required
def inbox_view(request):
    # Fetch unread messages for the logged-in user using the custom manager
    unread_messages = (
        Message.unread_messages.unread_for_user(request.user)
        .select_related('sender')  # Optimize fetching of the sender information
        .order_by('timestamp')  # Order messages by timestamp
    )
    
    return render(request, 'messaging/inbox.html', {'unread_messages': unread_messages})



@login_required
@cache_page(60)  # Cache this view for 60 seconds
def conversation_view(request):
    # Fetch messages for the logged-in user
    messages = (
        Message.objects.select_related('sender')
        .filter(receiver=request.user)
        .order_by('timestamp')
    )
    
    return render(request, 'messaging/conversation.html', {'messages': messages})