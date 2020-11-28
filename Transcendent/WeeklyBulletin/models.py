from django.db import models

# Create your models here.

class Articles(models.Model):
    Editorial='ed'
    Science='sc'
    Sports='sp'
    News='nw'
    Business='bs'
    Leisure='ls'
    title=models.CharField(max_length=25)
    matter=models.TextField()
    category_choices=[(Editorial,'Editorial'),(Science,'Science'),(Business,'Business'),(Leisure,'Leisure'),(Sports,'Sports'),(News,'News'),]
    category=models.CharField(max_length=2,choices=category_choices,default=Editorial)
    date=models.DateField()
    img=models.ImageField(upload_to='images')
    author=models.CharField(max_length=25)