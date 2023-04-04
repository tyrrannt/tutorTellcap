from django.contrib import admin

from courseapp.models import Course, CourseModule

# Register your models here.

admin.site.register(Course)
admin.site.register(CourseModule)
