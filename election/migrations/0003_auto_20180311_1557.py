# Generated by Django 2.0.2 on 2018-03-11 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0002_voter'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='name',
            field=models.CharField(default='votername', max_length=30),
        ),
        migrations.AddField(
            model_name='voter',
            name='roll',
            field=models.CharField(default='rollno', max_length=7),
        ),
    ]
