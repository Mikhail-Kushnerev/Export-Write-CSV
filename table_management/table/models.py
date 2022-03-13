from django.db import models


class Student(models.Model):
    roll = models.CharField(max_length=200, default='')
    sclass = models.CharField(max_length=200, default='')
    fname = models.CharField(max_length=200, default='')
    lname = models.CharField(max_length=200, default='')