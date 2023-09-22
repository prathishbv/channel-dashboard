
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Device

class DeviceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'device_updates'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

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
        
