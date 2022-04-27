import imp
from pyexpat import model
import random
from statistics import mode
from django.db import models
from myversity.models import LoginSite, Registration


choice_department = (
    ("CSE", "CSE"),
    ("ENGLISH", "ENGLISH"),
    ("BBA", "BBA"),
    ("BANGLA", "BANGLA"),
    ("ISLAMIC STUDIES", "ISLAMIC STUDIES"),
    ("EEE", "EEE"),
)

Maritial_Status = (
    ("Married", "Married"),
    ("UnMarried", "UnMarried"),
)
Gender = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Others", "Others"),
)

Religion = (
    ("Islam", "Islam"),
    ("Hindu", "Hindu"),
    ("Christianity", "Christianity"),
    ("Buddhism", "Buddhism"),
)

Group = (
    ("Science", "Science"),
    ("ARS", "ARS"),
    ("Business", "Business"),

)
Board = (
    ("Sylhet", "Sylhet"),
    ("Dhaka", "Dhaka"),
    ("Khulna", "Khulna"),
    ("Rajshahi", "Rajshahi"),

)

Year = (
    ("2000", "2000"),
    ("2001", "2001"),
    ("2002", "2002"),
    ("2003", "2003"),

)


class Student_All_Info(models.Model):
    user = models.ForeignKey(
        Registration, on_delete=models.CASCADE, null=True, blank=True)
    departMent = models.CharField(
        max_length=200, choices=choice_department, default="CSE")
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    maritial_status = models.CharField(
        max_length=200, choices=Maritial_Status, default="Unmarried")
    blood_Group = models.CharField(max_length=10)
    national_id = models.IntegerField()
    d_o_birth = models.DateField()
    gender = models.CharField(max_length=200, choices=Gender, default="Male")
    religion = models.CharField(
        max_length=200, choices=Religion, default="Islam")
    nationality = models.CharField(max_length=100)
    guardians_name = models.CharField(max_length=100)
    guardians_con_no = models.IntegerField()
    permanent_address = models.TextField()
    present_address = models.TextField()
    registration_no_of_ssc = models.IntegerField()
    name_of_instituin_ssc = models.CharField(max_length=100)
    roll_ssc = models.IntegerField()
    group_ssc = models.CharField(max_length=200, choices=Group, default="Male")
    year_ssc = models.CharField(max_length=200, choices=Year, default="2016")
    Board_ssc = models.CharField(
        max_length=200, choices=Board, default="Science")
    gpa_ssc = models.FloatField()
    registration_no_of_hsc = models.IntegerField()
    name_of_instituin_hsc = models.CharField(max_length=100)
    roll_hsc = models.IntegerField()
    group_hsc = models.CharField(max_length=200, choices=Group, default="Male")
    year_hsc = models.CharField(max_length=200, choices=Year, default="2016")

    Board_hsc = models.CharField(
        max_length=200, choices=Board, default="Science")
    gpa_hsc = models.FloatField()
    student_Img = models.ImageField(upload_to='studentimages/')
