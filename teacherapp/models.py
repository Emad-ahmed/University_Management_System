from django.db import models

# Create your models here.
import imp
import random
from statistics import mode
from django.db import models


semister_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
)


class Deparetment(models.Model):
    department_code = models.CharField(max_length=100)
    dep_name = models.CharField(max_length=240)

    def __str__(self):
        return self.dep_name


class Course(models.Model):
    course_code = models.CharField(max_length=100)
    course_name = models.CharField(max_length=240)
    credit = models.IntegerField()
    description = models.TextField()
    deparetment = models.ForeignKey(Deparetment, on_delete=models.CASCADE)
    semister = models.CharField(
        choices=semister_CHOICES, max_length=50, default="1")

    def __str__(self):
        return self.deparetment.dep_name
