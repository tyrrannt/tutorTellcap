# Generated by Django 4.2 on 2023-04-10 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0009_siteevents_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteevents',
            name='location',
            field=models.CharField(default='', max_length=100, verbose_name='Место проведения'),
        ),
    ]
