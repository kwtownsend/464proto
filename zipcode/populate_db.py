import csv

from django.core.management.base import BaseCommand
from webapp.models import Zipcode
from locations.models import Cities



class Command(BaseCommand):
    # args = '<foo bar ...>'
    help = 'import lat lon zip info from file'


    def _delete_table_info(self):
        print("****** Deleting all table data for fresh import ******** ")
        Cities.objects.all().delete()


    def _import_from_csv(self):
        with open("zipcode/us_postal_codes.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                _, created = Cities.objects.get_or_create(
                    postalcode=row[0],
                    city=row[1],
                    state=row[2],
                    county=row[3],
                    latitude=row[4],
                    longitude=row[5],

                )
                print("Done")


    def handle(self, *args, **options):
        self._delete_table_info()
        self._import_from_csv()