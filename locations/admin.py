from django.contrib import admin
from locations.models import Zipcode, Cities


class ZipcodeAdmin(admin.ModelAdmin):
    list_display = ('zip', 'city', 'state', 'latitude', 'longitude', 'timezone', 'daylight_savings_time')


admin.site.register(Zipcode, ZipcodeAdmin)

class CitiesAdmin(admin.ModelAdmin):
	list_display = ('city', 'state', 'county', 'latitude', 'longitude')

admin.site.register(Cities, CitiesAdmin)


