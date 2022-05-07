import random
from django.db import models


while True:
    number = ''.join(str(x) for x in random.sample(range(10), 4))
    if not number.startswith('0'):
        break


choice_department = (
    ("CSE", "CSE"),
    ("ENGLISH", "ENGLISH"),
    ("BBA", "BBA"),
    ("BANGLA", "BANGLA"),
    ("ISLAMIC STUDIES", "ISLAMIC STUDIES"),
    ("EEE", "EEE"),
)


class Registration(models.Model):
    name = models.CharField(max_length=120)
    phone = models.IntegerField()
    email = models.EmailField()
    departMent = models.CharField(
        max_length=200, choices=choice_department, default="CSE")
    ssc_gpa = models.FloatField()
    hsc_gpa = models.FloatField()
    referece_number = models.CharField(
        max_length=7, default=number, unique=True)

    def isExists(self):
        if Registration.objects.filter(email=self.email):
            return True

        return False

    def isExists(self):
        if Registration.objects.filter(referece_number=self.referece_number):
            return True

        return False

    @staticmethod
    def get_student_by_email(email):
        try:
            return Registration.objects.get(email=email)
        except:
            return False
