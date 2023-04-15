from django.http import JsonResponse
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from courseapp.forms import CourseAddForm, CourseUpdateForm, SiteEventsAddForm, SiteEventsUpdateForm
from courseapp.models import Course, RelatedCourse, GoogleForm, SiteEvents
from re import sub as google_form


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

    def form_valid(self, form):
        return super().form_valid(form)

    def get_absolute_url(self):
        return reverse('courseapp:course_list')


def get_google_form(pattern):
    try:
        obj = GoogleForm.objects.get(name=pattern.group(0))
        url = f'<iframe src="{obj.url}" width="{obj.width}%" height="{obj.height}" seamless="seamless" frameborder="0" marginwidth="0" marginheight="0" html="Загрузка..."></iframe>'
    except Exception as _ex:
        return pattern.group(0)
    return url


def get_audio_file(pattern):
    try:
        url = f'<audio controls="controls" crossorigin="anonymous" style="width:100%;" controlsList="nodownload"><source src="/media/{pattern.group(0)}" type="audio/mpeg"></audio>'
    except Exception as _ex:
        return pattern.group(0)
    return url


class CourseItem(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_object = self.get_object()
        context['title'] = course_object
        content_text = course_object.content
        content_text = google_form(r'(GoogleForm\d+)', get_google_form, content_text)
        context['replase_content'] = content_text
        try:
            related_course = RelatedCourse.objects.get(from_course=course_object)
            context['related_course'] = related_course.to_course.all()

        except Exception as _ex:
            pass

        return context


class CourseUpdate(UpdateView):
    model = Course
    form_class = CourseUpdateForm


class SiteEventsList(ListView):
    model = SiteEvents


class SiteEventsSettingsList(ListView):
    model = SiteEvents
    template_name = 'courseapp/siteevents_settings_list.html'


class SiteEventsItem(DetailView):
    model = SiteEvents


class SiteEventsAdd(CreateView):
    model = SiteEvents
    form_class = SiteEventsAddForm


class SiteEventsUpdate(UpdateView):
    model = SiteEvents
    form_class = SiteEventsUpdateForm


class RelationSettingsList(ListView):
    model = RelatedCourse

