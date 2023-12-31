from django.urls import re_path
from .consumers import DeviceConsumer

# Route for websocket connection
websocket_urlpatterns = [
    re_path(r'ws/devices/$', DeviceConsumer.as_asgi()),
]
