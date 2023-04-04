from django import forms

from courseapp.models import Course


class CourseAddForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'logo', 'date_created', 'short_description', 'content')


class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'logo', 'date_created', 'short_description', 'content')
