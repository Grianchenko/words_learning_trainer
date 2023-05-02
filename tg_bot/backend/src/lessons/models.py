import datetime

from django.utils.timezone import now
from django.db import models

# Create your models here.


class Lessons(models.Model):
    date = models.DateField(verbose_name='Date', default=now().date())
    theme = models.CharField(verbose_name='Theme', max_length=200)
    homework = models.CharField(verbose_name='Homework', max_length=1000)
    mark = models.IntegerField(verbose_name='Mark', default=None)

