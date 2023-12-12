

# Register your models here.
# chatbot/admin.py
from django.contrib import admin
from .models import Conversation

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('user_input', 'bot_response', 'timestamp')
    search_fields = ('user_input', 'bot_response')
