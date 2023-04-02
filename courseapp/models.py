import datetime

from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.

class Course(models.Model):
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    name = models.CharField(verbose_name='Название', max_length=100)
    date_created = models.DateField(verbose_name='Дата создания', default=datetime.datetime.now())
    short_description = models.CharField(verbose_name='Краткое описание', max_length=120, blank=True)
    content = RichTextField(verbose_name='Описание', config_name='default', default='', blank=True)
