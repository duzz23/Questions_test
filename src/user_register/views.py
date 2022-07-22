from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.views.generic import TemplateView

from user_register.models import UserRegisterForm, UserLoginForm


class HomePage(TemplateView):
    template_name = 'user_register/base.html'

# Регистрации пользователя и в случае успеха переход на страницу с вопросами
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return render(request, 'answer/index.html', {"form": form})
        else:
            for message in form.error_messages:
                messages.error(request, message)
    else:
        form = UserRegisterForm()
    return render(request, 'user_register/register.html', {"form": form})

# Авторизация пользователя и в случае успеха переход на страницу с вопросами
def User_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('start/')

    else:
        form = UserLoginForm()
    return render(request, 'user_register/login.html', {"form": form})

# При выходе отправляемся на home page
def User_logout(request):
    logout(request)
    return redirect('home')
