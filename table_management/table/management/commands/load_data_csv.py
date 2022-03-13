from csv import DictReader
from django.core.management import BaseCommand

# Import the model 
from table.models import Student

CATALOG = {
    Student : 'table.csv'
}

class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from table.csv"

    def handle(self, *args, **kwargs):

        # # Show this if the data already exist in the database
        # if children.objects.exists():
        #     print('child data already loaded...exiting.')
        #     print(ALREDY_LOADED_ERROR_MESSAGE)
        #     return
            
        # # Show this before loading the data into the database
        print("Loading childrens data")

        for model, data in CATALOG.items():
        #Code to load the data into database
            for row in DictReader(
                open(f'./{data}', 'r'),
                delimiter=';',
                quotechar=',',
            ):
                created = model(
                    row['id'],
                    row['RollNo'],
                    row['Class'],
                    row['First Name'],
                    row['Last Name']
                )
                created.save()
        self.stdout.write(self.style.SUCCESS(' Ready '))
