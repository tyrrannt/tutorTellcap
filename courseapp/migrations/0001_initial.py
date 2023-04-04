# Generated by Django 4.1.7 on 2023-04-03 16:56

import courseapp.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('logo', models.ImageField(blank=True, upload_to=courseapp.models.course_directory_path, verbose_name='Логотип')),
                ('date_created', models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('short_description', models.CharField(blank=True, max_length=120, verbose_name='Краткое описание')),
                ('content', django_ckeditor_5.fields.CKEditor5Field(blank=True, default='', verbose_name='Text')),
                ('courses', models.BigIntegerField(default=0, verbose_name='Общее время')),
                ('courses_time', models.CharField(blank=True, choices=[('0', 'Min'), ('1', 'Hours'), ('2', 'Month'), ('3', 'Year')], default='', max_length=5, verbose_name='Измерение курса')),
                ('duration', models.BigIntegerField(default=0, verbose_name='Продолжительность')),
                ('duration_time', models.CharField(blank=True, choices=[('0', 'Min'), ('1', 'Hours'), ('2', 'Month'), ('3', 'Year')], default='', max_length=5, verbose_name='Измерение продолжительности')),
                ('cost', models.FloatField(default=0, verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='RelatedCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_with', to='courseapp.course')),
                ('to_course', models.ManyToManyField(related_name='related_courses', to='courseapp.course')),
            ],
            options={
                'verbose_name': 'Связанные курсы',
                'verbose_name_plural': 'Связанные курсы',
            },
        ),
        migrations.CreateModel(
            name='CourseModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('logo', models.ImageField(blank=True, upload_to=courseapp.models.course_directory_path, verbose_name='Логотип')),
                ('date_created', models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('short_description', models.CharField(blank=True, max_length=120, verbose_name='Краткое описание')),
                ('content', django_ckeditor_5.fields.CKEditor5Field(blank=True, default='', verbose_name='Text')),
                ('parent_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courseapp.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Модуль',
                'verbose_name_plural': 'Модули',
            },
        ),
    ]
