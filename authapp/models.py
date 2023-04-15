from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


# Create your models here.

class CustomUser(AbstractUser):
    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователя'

    avatar = models.ImageField(upload_to='Аватар', blank=True)
    birthday = models.DateField(verbose_name='День рождения', blank=True, null=True)
    activate_key = models.CharField(verbose_name='Код активации', max_length=128, blank=True, null=True)
    superintendent = models.BooleanField(verbose_name='Сотрудник', default=False)
    surname = models.CharField(verbose_name='Отчетство', max_length=25, default='', blank=True)
    personal_code = models.CharField(verbose_name='Персональный код', max_length=4, default='', blank=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    def get_absolute_url(self):
        return reverse('authapp:users_list')
