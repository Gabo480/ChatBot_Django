# chatbot_project/urls.py
from django.contrib import admin
from django.urls import path, include  # Importa 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chatbot.urls')),  # Agrega esta línea para redireccionar a 'chatbot'
]
