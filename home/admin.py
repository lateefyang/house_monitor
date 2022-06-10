from django.contrib import admin

from . import models


class DeviceAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Device, DeviceAdmin)
