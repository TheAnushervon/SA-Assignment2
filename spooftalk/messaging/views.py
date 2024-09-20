from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .models import Message
# Create your views here.


class MessagesCountAPIView(APIView):
    def get(self, request, format=None):
        data = {
            "messages_count": Message.objects.all().count(),
        }
        return Response(data, status=status.HTTP_200_OK)


def messaging(request):
    queryset = Message.objects.all()
    return render(request, 'messaging.html', {'message': queryset})


def index(request):
    return render(request, 'index.html')
