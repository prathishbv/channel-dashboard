from rest_framework import serializers
from .models import Device

# Responsible for converting objects into data types understandable by Tkinter application 
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'device_name', 'status', 'last_update_time']
