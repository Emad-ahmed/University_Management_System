import email
import imp
import random
from statistics import mode
from django.db import models


class LoginSite(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email
