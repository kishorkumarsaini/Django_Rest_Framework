from django.db import models

# Create your models here.

class Singer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    title=models.CharField(max_length=120)
    description=models.TextField()
    singer=models.ForeignKey(Singer,on_delete=models.CASCADE)

    def __str__(self):
        return self.title