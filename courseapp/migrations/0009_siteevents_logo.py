# Generated by Django 4.2 on 2023-04-10 13:19

import courseapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0008_alter_siteevents_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteevents',
            name='logo',
            field=models.ImageField(blank=True, upload_to=courseapp.models.events_directory_path, verbose_name='Логотип'),
        ),
    ]
