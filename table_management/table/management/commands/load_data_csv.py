from csv import DictReader
from django.core.management import BaseCommand

# Import the model 
from table.models import Student


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from table.csv"

    def handle(self, *args, **options):


        # # Show this if the data already exist in the database
        # if children.objects.exists():
        #     print('child data already loaded...exiting.')
        #     print(ALREDY_LOADED_ERROR_MESSAGE)
        #     return
            
        # # Show this before loading the data into the database
        # print("Loading childrens data")


        #Code to load the data into database
        for row in DictReader(open('./table.csv', 'r'), delimiter=';', quotechar=','):
            child=Student(
                row['id'],
                row['RollNo'],
                row['Class'],
                row['First Name'],
                row['Last Name']
            )
            child.save()