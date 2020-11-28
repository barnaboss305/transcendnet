from django.db import models

# Create your models here.

class Articles(models.Model):
    title=models.CharField(max_length=25)
    matter=models.TextField()
    date=models.DateField()
    img=models.ImageField(upload_to='images')
    author=models.CharField(max_length=25)