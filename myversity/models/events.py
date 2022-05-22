import imp
import random
from statistics import mode
from django.db import models


class Events(models.Model):
    title = models.CharField(max_length=250)
    alldes = models.TextField()
    eventsimg = models.ImageField(upload_to='eventsimages/')
