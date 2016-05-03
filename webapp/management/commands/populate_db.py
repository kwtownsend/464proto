import csv

from django.core.management.base import BaseCommand
from webapp.models import Zipcode


class Command(BaseCommand):
    # args = '<foo bar ...>'
    help = 'import lat lon zip info from file'


    def _delete_table_info(self):
        print("****** Deleting all table data for fresh import ******** ")
        Zipcode.objects.all().delete()


    def _import_from_csv(self):
        with open("zipcode/zipcode.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                print("zip is " + row[0])
                if row[6]==1:
                    dst=True
                else:
                    print(row[0])
                    print(row[1])
                    print(row[2])
                    print("not using daylight savings time")
                    dst=False
                _, created = Zipcode.objects.get_or_create(
                    zip=row[0],
                    city=row[1],
                    state=row[2],
                    latitude=row[3],
                    longitude=row[4],
                    timezone=row[5],
                    daylight_savings_time=dst,
                )


    def handle(self, *args, **options):
        self._delete_table_info()
        self._import_from_csv()

