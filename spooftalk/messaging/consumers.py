import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from messaging.models import Message
from datetime import datetime


class MessengerConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = "chat"

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        Message.objects.create(text=message)
        if (Message.objects.all().count() > 0):
            timestamp = Message.objects.last().timestamp.isoformat()
        else:
            timestamp = datetime.now().isoformat()
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.message",
                                   "message": message, "timestamp": timestamp}
        )

    def chat_message(self, event):
        message = event["message"]
        timestamp = event["timestamp"]

        self.send(text_data=json.dumps(
            {"message": message, "timestamp": timestamp}))
