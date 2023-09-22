from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Device
from rest_framework.authtoken.models import Token 
from django.conf import settings

# This will be triggered when there is any change in the Device model and updates the channel for asynchronous communication
@receiver(post_save, sender=Device)
def device_update_notification(sender, instance, created, **kwargs):
    if created:
        action = 'created'
    else:
        action = 'updated'
    
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'device_updates',
        {
            'type': 'device.update',
            'action': action,
            'device_id': instance.id,
            'device_name': instance.device_name,
            'status': instance.status,
            'last_update_time': instance.last_update_time.isoformat(),
        }
    )


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)