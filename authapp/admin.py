from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authapp.models import CustomUser


# Register your models here.

class CustomUserAdmin(UserAdmin):
    """
    Расширяем модель UserAdmin
    fieldsets: исходный набор полей формы
    *UserAdmin.fieldsets: добавляем расширенный набор полей формы,
        тип: кортеж содержащий ('заголовок группы по вашему выбору', {словарь c новыми полями})
    """
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Профиль',
            {
                'fields': (
                    'surname', 'superintendent', 'personal_code', 'avatar',
                ),
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
