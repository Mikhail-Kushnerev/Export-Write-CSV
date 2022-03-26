from csv import DictReader

from django.core.management import BaseCommand
from table.models import Student

CATALOG = {
    Student : 'table.csv'
}

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        print('\tstart Scanning')

        for model, data in CATALOG.items():

            print(f'Loading {data} data')
            
            for row in DictReader(
                open(f'static/data/{data}', 'r'),
                delimiter=';',
                quotechar=',',
            ):
                created = model(
                    id=row['id'],
                    roll=row['RollNo'],
                    sclass=row['Class'],
                    fname=row['First Name'],
                    lname=row['Last Name']
                )
                created.save()
        self.stdout.write(self.style.SUCCESS(' Ready '))
