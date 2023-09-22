from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Device

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
