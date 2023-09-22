from django.urls import path
from .views import DeviceListCreateAPIView, DeviceRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('devices/', DeviceListCreateAPIView.as_view(), name='device-list-create'),
    path('devices/<int:pk>/', DeviceRetrieveUpdateDestroyAPIView.as_view(), name='device-retrieve-update-destroy'),
]
