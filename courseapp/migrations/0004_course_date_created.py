# Generated by Django 4.1.7 on 2023-04-02 21:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0003_course_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2023, 4, 2, 21, 44, 14, 694122), verbose_name='Дата создания'),
        ),
    ]
