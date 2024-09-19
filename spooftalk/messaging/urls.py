from .views import MessagesCountAPIView, index
from django.urls import path

urlpatterns = [
    path('count/', MessagesCountAPIView.as_view(), name='messages_count'),
    path('', index)
]
