from django.shortcuts import render, get_object_or_404
from .models import Message
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User

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