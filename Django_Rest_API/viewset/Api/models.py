from django.db import models

# Create your models here.
class Hero(models.Model):
    name=models.CharField(max_length=120)
    alias=models.CharField(max_length=120)


    def __str__(self):
        return self.name