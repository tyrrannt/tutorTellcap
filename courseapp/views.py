from django.views.generic import ListView, CreateView, DetailView, UpdateView

from courseapp.forms import CourseAddForm, CourseUpdateForm
from courseapp.models import Course


# Create your views here.

class CourseList(ListView):
    model = Course


class CourseAdd(CreateView):
    model = Course
    form_class = CourseAddForm


class CourseItem(DetailView):
    model = Course


class CourseUpdate(UpdateView):
    model = Course
    form_class = CourseUpdateForm
