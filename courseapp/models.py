from django.db import models

# Create your models here.

class Course(models.Model):
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    name = models.CharField(verbose_name='Название', max_length=100)
