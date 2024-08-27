from django.urls import path

from chat.consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/<str:room>/', ChatConsumer.as_asgi(),),
]
