# Generated by Django 2.0.1 on 2018-03-15 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0009_auto_20180314_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='avatar',
            field=models.ImageField(default='https://upload.wikimedia.org/wikipedia/commons/6/67/User_Avatar.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='avatar',
            field=models.ImageField(default='https://upload.wikimedia.org/wikipedia/commons/6/67/User_Avatar.png', upload_to=''),
        ),
    ]