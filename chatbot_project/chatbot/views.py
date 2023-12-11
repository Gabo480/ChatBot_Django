

# Create your views here.
# chatbot/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Conversation
import openai

def chat_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')

        # Llamada a OpenAI GPT-3 para obtener la respuesta del chatbot
        openai.api_key = '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'
        bot_response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=user_input,
            max_tokens=150
        )['choices'][0]['text']

        # Guardar la conversación en la base de datos
        Conversation.objects.create(
            user_input=user_input,
            bot_response=bot_response
        )

        return JsonResponse({'bot_response': bot_response})

    return render(request, 'chatbot/chat.html')
