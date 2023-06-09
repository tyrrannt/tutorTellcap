from django.urls import path

import authapp.views

app_name = 'authapp'

urlpatterns = [
    path('', authapp.views.index, name='index'),
    path('login/', authapp.views.login, name='login'),
    path('logout/', authapp.views.logout, name='logout'),
    path('register/', authapp.views.registration, name='register'),
    path('list/', authapp.views.CustomUserList.as_view(), name='users_list'),
    path('update/<int:pk>/', authapp.views.CustomUserUpdate.as_view(), name='users_update'),
]
