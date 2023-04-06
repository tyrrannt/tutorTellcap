from django import forms
from django_ckeditor_5.fields import CKEditor5Field
from django_ckeditor_5.widgets import CKEditor5Widget

from courseapp.models import Course


class CourseAddForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ('name', 'logo', 'date_created', 'short_description', 'content', 'courses', 'courses_time', 'duration', 'duration_time', 'cost')
        widgets = {
            "content": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            )
        }

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы под Bootstrap
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form form-control', 'autocomplete': 'off'})

        self.fields['content'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})
        self.fields['content'].required = False


class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'logo', 'date_created', 'short_description', 'content', 'courses', 'courses_time', 'duration', 'duration_time', 'cost')
