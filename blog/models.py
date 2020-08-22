from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=25, default="Me")
    publicated_data = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
