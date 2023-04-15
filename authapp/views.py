from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_obj
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from authapp.forms import UserLoginForm, SignUpForm, CustomUserUpdateForm
from authapp.models import CustomUser


# Create your views here.


def show_404(request, exception=None):
    return render(request, 'authapp/404.html')


def index(request):
    return render(request, 'authapp/base.html')


def login(request):
    title = ':: TELLCAP :: Авторизация'

    if request.method == 'POST':
        login_form = UserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                request.session.set_expiry(3600)
                return HttpResponseRedirect(reverse('authapp:index'))
    else:
        login_form = UserLoginForm()
    content = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/base.html', {'form': login_form})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('courseapp:course_list'))


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login_obj(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'authapp/base.html', {'form': form})


class CustomUserList(ListView):
    model = CustomUser


class CustomUserUpdate(UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
