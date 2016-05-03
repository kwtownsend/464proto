from django.db import models


class Zipcode(models.Model):
    zip = models.PositiveIntegerField(primary_key=True)
    city =  models.CharField(max_length=27)
    state = models.CharField(max_length=2)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timezone = models.SmallIntegerField()
    daylight_savings_time = models.BooleanField(default=True)

    def lat_lon_from_zip(self, zip):
        geo_record = Zipcode.object.get(pk=zip)
        if geo_record:
            print("the type of the latitude is:")
            print(type(geo_record.latitude))
            return geo_record.latitude, geo_record.longitude
        else:
            print("zip not found: give CSUF zip")
            return 33.640302, -117.769442

