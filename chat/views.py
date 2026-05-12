from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import ChatSession, ChatMessage
import json

from .ai_agent import graph, SYSTEM_PROMPT, parse_response

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'chat/register.html', {'form': form})

@login_required
def chat_interface(request, session_id=None):
    sessions = ChatSession.objects.filter(user=request.user).order_by('-created_at')
    active_session = get_object_or_404(ChatSession, id=session_id, user=request.user) if session_id else None
    messages = active_session.messages.all().order_by('timestamp') if active_session else []

    return render(request, 'chat/index.html', {
        'sessions': sessions,
        'active_session': active_session,
        'messages': messages,
    })

@login_required
def new_chat(request):
    session = ChatSession.objects.create(user=request.user, title="New Conversation")
    return redirect('chat_interface_with_id', session_id=session.id)

@login_required
def send_message(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message")
        session_id = data.get("session_id")
        
        session = get_object_or_404(ChatSession, id=session_id, user=request.user)
        ChatMessage.objects.create(session=session, role="user", content=user_message)

        try:
            inputs = {"messages": [("system", SYSTEM_PROMPT), ("user", user_message)]}
            stream = graph.stream(inputs, stream_mode="updates")
            tool_name, ai_response = parse_response(stream)
            if not ai_response:
                ai_response = "I am here to listen. Could you please tell me more?"
        except Exception as e:
            ai_response = f"An error occurred: {str(e)}"
            tool_name = "Error"

        ChatMessage.objects.create(session=session, role="assistant", content=ai_response, tool_called=tool_name)
        return JsonResponse({"status": "success", "session_id": session.id, "response": ai_response, "tool_called": tool_name})
    return JsonResponse({"status": "error", "message": "Invalid request"})