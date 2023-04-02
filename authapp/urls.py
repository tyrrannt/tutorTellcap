from django.urls import path

import authapp.views

app_name = 'authapp'

urlpatterns = [
    path('', authapp.views.index, name='index'),
    path('login/', authapp.views.login, name='login'),
    path('logout/', authapp.views.logout, name='logout'),

]
