import random
from django.db import models


while True:
    number = ''.join(str(x) for x in random.sample(range(10), 4))
    if not number.startswith('0'):
        break


class Registration(models.Model):
    name = models.CharField(max_length=120)
    phone = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    departMent = models.CharField(max_length=30)
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
