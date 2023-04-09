from django.urls import path

import courseapp.views

app_name = 'courseapp'

urlpatterns = [
    # path('', authapp.views.index, name='index'),
    path('list/', courseapp.views.CourseList.as_view(), name='course_list'),
    path('settings/', courseapp.views.CourseSettingsList.as_view(), name='course_settings_list'),
    path('add/', courseapp.views.CourseAdd.as_view(), name='course_add'),
    path('<int:pk>/', courseapp.views.CourseItem.as_view(), name='course'),
    path('update/<int:pk>/', courseapp.views.CourseUpdate.as_view(), name='course_update'),
    # path('logout/', authapp.views.logout, name='logout'),
    path('events-list/', courseapp.views.SiteEventsList.as_view(), name='events_list'),
]
