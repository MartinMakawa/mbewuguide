import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatGroup, GroupMessage
from django.contrib.auth.models import AnonymousUser

class ChatroomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chatroom_name = self.scope['url_route']['kwargs']['chatroom_name']
        self.room_group_name = f"chat_{self.chatroom_name}"

        self.user = self.scope.get("user", AnonymousUser())
        if not self.user.is_authenticated:
            # Reject connection if not authenticated
            await self.close()
            return
        await self.accept()

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        if not self.user.is_authenticated:
            await self.send(text_data=json.dumps({'error': 'Authentication required to send messages.'}))
            return
        data = json.loads(text_data)
        message = data.get('message')
        if not message:
            await self.send(text_data=json.dumps({'error': 'Message content required.'}))
            return
        # Save message to database (sync to async)
        from asgiref.sync import sync_to_async
        try:
            group = await sync_to_async(ChatGroup.objects.get)(group_name=self.chatroom_name)
            await sync_to_async(GroupMessage.objects.create)(
                group=group,
                author=self.user,
                body=message
            )
        except ChatGroup.DoesNotExist:
            await self.send(text_data=json.dumps({'error': 'ChatGroup not found.'}))
            return
        # Broadcast message to group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': self.user.username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))
