from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from courseapp.models import Course


# Create your views here.

class CourseList(ListView):
    model = Course

class CourseAdd(CreateView):
    model = Course

class CourseItem(DetailView):
    model = Course

class CourseUpdate(UpdateView):
    model = Course


