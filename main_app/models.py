from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Shoe(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=25)
    size = models.IntegerField()
    colorway = models.CharField(max_length=15)
    description = models.TextField(max_length=200)
    release_date = models.DateField('Release Date')
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'





