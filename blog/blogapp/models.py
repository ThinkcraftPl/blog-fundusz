from django.db import models

# Create your models here.
class Wpis(models.Model):
    tytul = models.CharField(max_length=100)
    tresc = models.CharField(max_length=140)
    gram = models.IntegerField()
    objects = models.Manager()