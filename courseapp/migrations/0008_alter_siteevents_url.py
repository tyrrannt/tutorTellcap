# Generated by Django 4.2 on 2023-04-10 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0007_siteevents_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteevents',
            name='url',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Ссылка'),
        ),
    ]