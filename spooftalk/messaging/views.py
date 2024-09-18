from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class MessagesCountAPIView(APIView):
    def get(self, request, format=None):
        data = {
            "messages_count": 50,
        }
        return Response(data, status=status.HTTP_200_OK)
