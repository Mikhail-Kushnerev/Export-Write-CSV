from email import header
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Student
from django.http import HttpResponse

import csv


def export_csv(request):
    students = Student.objects.all()
    response = HttpResponse(
        content_type='text/csv',
        headers = {'Сохранить как': 'attachment; filename=students.csv'}
    )
    #* response['Content-Disposition'] = 'attachment; filename=students.csv'
    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response, delimiter=';')
    writer.writerow(['RollNo', 'Class', 'First Name', 'Last Name'])
    #* studs = students.values_list('id','roll', 'sclass', 'fname', 'lname')
    for std in students:
    #* for std in studs:
        #* writer.writerow(std)
        writer.writerow(
            [
                std.roll,
                std.sclass,
                std.fname,
                std.lname,
            ]
        )
    return response