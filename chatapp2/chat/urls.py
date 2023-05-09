from django.urls import path
from . import views

urlpatterns = [
    path('', views.lobby, name = 'lobby'),
    path('chat/<str:room_code>/',views.chat, name = 'chat')
]

