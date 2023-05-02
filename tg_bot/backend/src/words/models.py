from django.db import models

# Create your models here.


class Words(models.Model):
    word = models.CharField(verbose_name='Word', max_length=25)
    translation = models.CharField(verbose_name='Translation', max_length=100)

    def __str__(self):
        return f'{self.word} --- {self.translation}'

