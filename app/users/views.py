from django.contrib import auth
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

from .forms import UserRegisterForm, UserLoginForm


class UserRegisterView(CreateView):
    """
    Форма для регистрации нового пользователя
    """
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("home:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Регистрация"
        return context


class UserLoginView(LoginView):
    """
    Авторизация на сайте
    """
    form_class = UserLoginForm
    template_name = "users/login.html"
    next_page = 'home:home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Login"
        return context


class UserLogoutView(LogoutView):
    """
    Выход из аккаунта
    """
    next_page = "home:home"


class UserAccountView(View):
    """
    Профиль пользователя
    """

    def get(self, request, *args, **kwargs):
        return render(request, "users/account.html")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Account"
        return context
