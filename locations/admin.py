from django.contrib import admin
from locations.models import Zipcode


class ZipcodeAdmin(admin.ModelAdmin):
    list_display = ('zip', 'city', 'state', 'latitude', 'longitude', 'timezone', 'daylight_savings_time')


admin.site.register(Zipcode, ZipcodeAdmin)
