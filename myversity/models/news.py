import imp
import random
from statistics import mode
from django.db import models
from myversity.models import Registration


class News(models.Model):
    title = models.CharField(max_length=250)
    allnmews = models.TextField()
    news_phot = models.ImageField(upload_to='newsimages/')
