import imp
import random
from statistics import mode
from django.db import models


class LoginSite(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)

    @staticmethod
    def get_student_by_email(email):
        try:
            return LoginSite.objects.get(email=email)
        except:
            return False
    

    
