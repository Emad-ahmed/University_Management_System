import imp
import random
from statistics import mode
from django.db import models

Department_CHOICES = (
    ('CSE', 'Department of CSE'),
    ('BBA', 'Department of Business Administration'),
    ('Law', 'Department of Law'),
    ('Architecture', 'Department of Architecture'),
    ('EEE', 'Department of EEE'),
    ('English', 'Department of English'),
    ('Civil', 'Department of Civil Engineering'),

)


class Teacher(models.Model):
    name = models.CharField(max_length=250)
    postion = models.CharField(max_length=250)
    department = models.CharField(
        max_length=50, choices=Department_CHOICES, default="CSE")
    cell_number = models.IntegerField()
    email = models.EmailField()
    biography = models.TextField()
    area_of_study = models.TextField()
    eventsimg = models.ImageField(upload_to='departnentimages/')

    def __str__(self):
        return self.name
