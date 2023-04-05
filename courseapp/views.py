from django.http import JsonResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from courseapp.forms import CourseAddForm, CourseUpdateForm
from courseapp.models import Course, RelatedCourse


# Create your views here.

class CourseList(ListView):
    model = Course


class CourseSettingsList(ListView):
    model = Course
    template_name = 'courseapp/course_settings_list.html'

    def get(self, request, *args, **kwargs):
        # Определяем, пришел ли запрос как JSON? Если да, то возвращаем JSON ответ
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            course_list = Course.objects.all()
            data = [course_item.get_data() for course_item in course_list]
            response = {'data': data}
            print(response)
            return JsonResponse(response)
        return super().get(request, *args, **kwargs)



class CourseAdd(CreateView):
    model = Course
    form_class = CourseAddForm


class CourseItem(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_object = self.get_object()
        context['title'] = course_object
        try:
            related_course = RelatedCourse.objects.get(from_course=course_object)
            context['related_course'] = related_course.to_course.all()
        except Exception as _ex:
            pass
        return context

class CourseUpdate(UpdateView):
    model = Course
    form_class = CourseUpdateForm
