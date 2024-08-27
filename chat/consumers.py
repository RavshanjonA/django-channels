from pyexpat import expat_CAPI

from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User

from chat.models import Message, Room


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room = self.scope['url_route']['kwargs']['room']
        self.group = f'chat_{self.room}'
        await self.channel_layer.group_add(
            self.group, self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        self.channel_layer.group_discard(
            self.channel_layer,
            self.group
        )

    async def receive(self, text_data):
        msgd = json.loads(text_data)
        username = msgd["username"]
        room = msgd["room"]
        message = msgd["message"]
        await self.channel_layer.group_send(
            self.group, {
                'type': 'chat',
                'message': message,
                'username': username,
                'room': room,
            }
        )
        await self.save_msg_db(message=message, user=username, room=room)

    async def chat(self, event):
        message = event['message']
        username = event['username']
        room = event['room']
        await self.send(text_data=json.dumps({'message': message, 'username': username, 'room': room}))

    @sync_to_async
    def save_msg_db(self, message, user, room):
        room = Room.objects.get(slug=room)
        if user:
            user = User.objects.get(username=user)
        else:
            user = User.objects.get(username="anonim")
        Message.objects.create(room=room, user=user, body=message)
