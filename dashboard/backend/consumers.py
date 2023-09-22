
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async  
from .models import Device
from rest_framework.authtoken.models import Token

class DeviceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'device_updates'
        
        headers = self.scope.get('headers', {})
        authorization_value = None

        for key, value in headers:
            if key == b'authorization':
                authorization_value = value.decode('utf-8').split(' ')[1]
                break
        if authorization_value == None:
            await self.close()
        else:
            token = await self.get_token(authorization_value)
            if not token:
                await self.close()
            else:
                await self.channel_layer.group_add(
                    self.group_name,
                    self.channel_name
                )
                await self.accept()

    @database_sync_to_async
    def get_token(self, authorization_value):
        try:
            return Token.objects.get(key=authorization_value)
        except Token.DoesNotExist:
            return None


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def device_update(self, event):
        action = event['action']
        device_id = event['device_id']
        device_name = event['device_name']
        status = event['status']
        last_update_time = event['last_update_time']

        await self.send(text_data=json.dumps({
            'action': action,
            'device_id': device_id,
            'device_name': device_name,
            'status': status,
            'last_update_time': last_update_time
        }))
        
