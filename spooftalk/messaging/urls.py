from .views import MessagesCountAPIView, messaging
from django.urls import path

urlpatterns = [
    path('count/', MessagesCountAPIView.as_view(), name='messages_count'),
    path('', messaging, name='chat')
]
