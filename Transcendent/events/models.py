from django.db import models

# Create your models here.

class Events(models.Model):
    name=models.CharField(max_length=25)
    description=models.TextField()
    date=models.DateField()
    price=models.IntegerField(default=0)
    poster=models.ImageField(upload_to='images')
    g_link=models.TextField()