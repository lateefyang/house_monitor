from datetime import datetime

from django.shortcuts import render
from django.views.generic import CreateView

from .models import Device


class DeviceCreateView(CreateView):
    model = Device
    fields = ['name']
    success_url = '/'
    extra_context = {
        'today': datetime.today(),
        'devices': Device.objects.all()
    }


def home(request):
    return render(request, 'home/welcome.html', {
        'today': datetime.today(),
        'devices': Device.objects.all()
    })
