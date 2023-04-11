import uuid
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field
from django.db import models
from django.utils import timezone

from authapp.models import CustomUser


# Create your models here.

def course_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return f'course/{filename}'

def events_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return f'events/{filename}'


class GoogleForm(models.Model):
    class Meta:
        verbose_name = 'Google форма'
        verbose_name_plural = 'Google формы'

    name = models.CharField(verbose_name='Название', max_length=500, default='GoogleForm')
    url = models.URLField(verbose_name='Ссылка')
    width = models.CharField(verbose_name='Ширина в процентах', max_length=3, default='100')
    height = models.CharField(verbose_name='Высота в процентах', max_length=3, default='100')

    def __str__(self):
        return self.name


class BaseModule(models.Model):
    class Meta:
        abstract = True
    uin = models.CharField(verbose_name='УИН', max_length=37, default=uuid.uuid4)
    name = models.CharField(verbose_name='Название', max_length=100)
    logo = models.ImageField(verbose_name='Логотип', upload_to=course_directory_path, blank=True)
    date_created = models.DateField(verbose_name='Дата создания', default=timezone.now)
    short_description = models.CharField(verbose_name='Краткое описание', max_length=120, blank=True)
    content = CKEditor5Field('Text', config_name='extends', default='', blank=True)


class Course(BaseModule):
    choise_time = [
        ('0', 'Min'),
        ('1', 'Hours'),
        ('2', 'Month'),
        ('3', 'Year'),
    ]

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    courses = models.BigIntegerField(verbose_name='Общее время', default=0)
    courses_time = models.CharField(verbose_name='Измерение курса', choices=choise_time, help_text='',
                                    blank=True, default='', max_length=5)
    duration = models.BigIntegerField(verbose_name='Продолжительность', default=0)
    duration_time = models.CharField(verbose_name='Измерение продолжительности', choices=choise_time, help_text='',
                                     blank=True, default='', max_length=5)
    cost = models.FloatField(verbose_name='Стоимость', default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('courseapp:course_settings_list')



class RelatedCourse(models.Model):
    class Meta:
        verbose_name = 'Связанные курсы'
        verbose_name_plural = 'Связанные курсы'

    from_course = models.ForeignKey(Course, related_name='course_with', on_delete=models.SET_NULL, null=True,
                                    blank=True)
    to_course = models.ManyToManyField(Course, related_name='related_courses')


class CourseModule(BaseModule):
    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'

    parent_course = models.ForeignKey(Course, verbose_name='Курс', on_delete=models.SET_NULL, null=True, blank=True)


class SiteEvents(models.Model):
    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    title = models.CharField(verbose_name='Заголовок', max_length=100, default='')
    description = models.CharField(verbose_name='Описание', max_length=350, default='')
    location = models.CharField(verbose_name='Место проведения', max_length=100, default='')
    logo = models.ImageField(verbose_name='Логотип', upload_to=events_directory_path, blank=True)
    start_time = models.DateField(verbose_name='Начало события', default=timezone.now)
    end_time = models.DateField(verbose_name='Окончание события', default=timezone.now)
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True, blank=True)
    url = models.CharField(verbose_name='Ссылка', max_length=300, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    hero_slider = models.BooleanField(verbose_name='Отображать на слайдере', default=False)
    speaker = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courseapp:events_list')

@receiver(post_save, sender=SiteEvents)
def change_url(sender, instance, **kwargs):
    try:
        # Формируем URL
        if instance.content_type.model == 'course':
            if instance.url != f'/courses/{instance.object_id}/':
                instance.url = f'/courses/{instance.object_id}/'
                instance.save()
    except Exception as _ex:
        pass
        #logger.error(f'Ошибка при переименовании файла {_ex}')