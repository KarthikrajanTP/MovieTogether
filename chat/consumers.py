import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_code = self.scope['url_route']['kwargs']['room_code']
        self.room_group_name = f'chat_{self.room_code}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_type = data['type']

        if message_type == 'chat':
            message = data['message']
            username = data['username']
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'username': username,
                }
            )
        elif message_type == 'video_control':
            action = data['action']
            timestamp = data['timestamp']
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'video_control',
                    'action': action,
                    'timestamp': timestamp,
                }
            )
        elif message_type == 'video_metadata':
            file_size = data['file_size']
            duration = data['duration']
            # Broadcast metadata to all users
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'video_metadata',
                    'file_size': file_size,
                    'duration': duration,
                }
            )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        await self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message,
            'username': username
        }))

    async def video_control(self, event):
        action = event['action']
        timestamp = event['timestamp']
        await self.send(text_data=json.dumps({
            'type': 'video_control',
            'action': action,
            'timestamp': timestamp
        }))

    async def video_metadata(self, event):
        file_size = event['file_size']
        duration = event['duration']
        await self.send(text_data=json.dumps({
            'type': 'video_metadata',
            'file_size': file_size,
            'duration': duration
        }))
