from django.urls import path

from home import views

urlpatterns = [
    path('', views.home, name='device.list'),
    #path('device/new', views.DeviceCreateView.as_view(), name='device.new')
    path('device/new', views.DeviceCreateView.as_view(), name='device.new')
]
