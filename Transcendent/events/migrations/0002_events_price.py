# Generated by Django 3.1.3 on 2020-11-28 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
