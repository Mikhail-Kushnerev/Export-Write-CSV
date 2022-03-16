import csv

from datetime import datetime as dt
from django.shortcuts import render
from django.http import HttpResponse

from .models import Student


def export_csv(request):
    students = Student.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={dt.now()}.csv'
    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response, delimiter=';')
    writer.writerow(['RollNo', 'Class', 'First Name', 'Last Name'])
    #* studs = students.values_list('id','roll', 'sclass', 'fname', 'lname')
    for std in students:
    #* for std in studs:
        #* writer.writerow(std)
        writer.writerow(
            [
                std.id,
                std.roll,
                std.sclass,
                std.fname,
                std.lname,
            ]
        )
    return response