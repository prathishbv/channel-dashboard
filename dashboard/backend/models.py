
from django.db import models

class Device(models.Model):
    device_name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    last_update_time = models.DateTimeField(auto_now=True)
