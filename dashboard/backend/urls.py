from django.urls import path
from .views import DeviceListCreateAPIView, DeviceRetrieveUpdateDestroyAPIView
from rest_framework.authtoken import views


urlpatterns = [
    path('devices/', DeviceListCreateAPIView.as_view(), name='device-list-create'),
    path('devices/<int:pk>/', DeviceRetrieveUpdateDestroyAPIView.as_view(), name='device-retrieve-update-destroy'),
    path('api-token-auth/', views.obtain_auth_token),    
]
