# Generated by Django 4.2 on 2023-04-07 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0003_alter_course_uin_alter_coursemodule_uin'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='GoogleForm', max_length=500, verbose_name='Название')),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('width', models.CharField(default='100', max_length=3, verbose_name='Ширина в процентах')),
                ('height', models.CharField(default='100', max_length=3, verbose_name='Высота в процентах')),
            ],
            options={
                'verbose_name': 'Google форма',
                'verbose_name_plural': 'Google формы',
            },
        ),
    ]