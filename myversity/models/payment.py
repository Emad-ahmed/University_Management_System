import imp
import random
from statistics import mode
from django.db import models
from myversity.models import Registration


class Payment_Done(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    payment_amount = models.IntegerField()
