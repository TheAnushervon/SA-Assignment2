from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path(r"ws/messaging/", consumers.MessengerConsumer.as_asgi(),
         name="messaging")
]
