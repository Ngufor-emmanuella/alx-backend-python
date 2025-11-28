from django.shortcuts import render, get_object_or_404
from .models import Message
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User

from django.shortcuts import render

def message_detail(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    history = message.history.all()  # Retrieve all historical edits
    return render(request, 'messaging/message_detail.html', {'message': message, 'history': history})



@login_required
def delete_user(request):
    if request.method == "POST":
        user = request.user
        user.delete()  # This will trigger the post_delete signal
        messages.success(request, "Your account has been deleted successfully.")
        return redirect('home')  # Redirect to a home or landing page
    return render(request, 'messaging/delete_user.html')


@login_required
def conversation_view(request):
    # Fetch all messages sent by the current user along with their replies
    messages = (
        Message.objects.select_related('sender', 'receiver')  # Optimize querying sender and receiver
        .prefetch_related('replies')  # Fetch all replies in a single query
        .filter(sender=request.user)  # Retrieve messages sent by the logged-in user
        .order_by('timestamp')  # Order messages by timestamp
    )
    return render(request, 'messaging/conversation.html', {'messages': messages})


def get_replies(message):
    replies = Message.objects.filter(parent_message=message).prefetch_related('replies')
    for reply in replies:
        reply.replies = get_replies(reply)  # Recursive call to get nested replies
    return replies