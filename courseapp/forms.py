from django import forms
from django_ckeditor_5.fields import CKEditor5Field
from django_ckeditor_5.widgets import CKEditor5Widget

from courseapp.models import Course


class CourseAddForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditor5Field(), label='')
    class Meta:
        model = Course
        fields = ('name', 'logo', 'date_created', 'short_description', 'content')
        widgets = {
            "text": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            )
        }


class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'logo', 'date_created', 'short_description', 'content')
