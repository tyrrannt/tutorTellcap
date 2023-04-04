from django_ckeditor_5.fields import CKEditor5Field
from django.db import models
from django.utils import timezone


# Create your models here.

def course_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return f'course/{filename}'


class BaseModule(models.Model):
    class Meta:
        abstract = True

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
