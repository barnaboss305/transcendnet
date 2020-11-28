from django.db import models

# Create your models here.

class Newsletter(models.Model):
    edition=models.CharField(max_length=25)
    poster=models.ImageField(upload_to='images')
    date=models.DateField()