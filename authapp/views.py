from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import UserLoginForm


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
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('authapp:index'))
