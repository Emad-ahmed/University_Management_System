from pyexpat import model
from django.db import models

# Create your models here.
import imp
import random
from statistics import mode
from django.db import models
from myversity.models.faculty import Teacher
from myversity.models.loginregister import LoginSite

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

semister_grade = (
    ('A+', 'A+'),
    ('A', 'A'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B', 'B'),
    ('B-', 'B-'),
    ('C+', 'C+'),
    ('C', 'C'),
    ('D', 'D'),
    ('F', 'F'),

)


class Deparetment(models.Model):
    department_code = models.CharField(max_length=100)
    dep_name = models.CharField(max_length=240)

    def __str__(self):
        return self.dep_name


class Course(models.Model):
    course_code = models.CharField(
        max_length=100, unique=True, default="n")
    course_name = models.CharField(
        max_length=240, unique=True, default="n")
    credit = models.IntegerField()
    description = models.TextField()
    deparetment = models.ForeignKey(Deparetment, on_delete=models.CASCADE)
    semister = models.CharField(
        choices=semister_CHOICES, max_length=50, default="1")

    def __str__(self):
        return self.course_code


class CourseAssign(models.Model):
    department = models.ForeignKey(Deparetment, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Result(models.Model):
    student = models.ForeignKey(LoginSite, on_delete=models.CASCADE)
    id_no = models.IntegerField()
    department = models.ForeignKey(Deparetment, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    select_grade = models.CharField(
        choices=semister_grade, max_length=50, default="A")


class SemisterRegister(models.Model):
    student = models.ForeignKey(LoginSite, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
