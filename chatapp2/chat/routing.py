from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('chat/<room_code>',consumers.ChatConsumer.as_asgi())
]