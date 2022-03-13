from django.db import models
from datetime import datetime as dt
from django.core.validators import MinValueValidator, MaxValueValidator


class Student(models.Model):
    roll = models.CharField(max_length=200)
    sclass = models.CharField(max_length=200)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)