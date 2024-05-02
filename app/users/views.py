from typing import Any
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views import View
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import login

from app.users.models import UserModel
from .mixins import UserIsNotAuth
from .forms import UserRegisterForm, UserLoginForm, UserForgotPasswordForm, UserSetNewPasswordForm
from .email import send_activate_user


class UserRegisterView(CreateView, UserIsNotAuth):
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

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        send_activate_user(user.id)
        return redirect("home:home")


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


class UserAddressView(View):
    """
    Профиль пользователя просмотр адреса
    """

    def get(self, request):
        return render(request, "users/address.html")

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Address"
        return context


class UserForgotPasswordView(PasswordResetView):
    """
    Представление по сбросу пароля по почте
    """
    form_class = UserForgotPasswordForm
    template_name = "users/registration/user_password_reset.html"
    success_url = reverse_lazy("home:home")
    subject_template_name = "users/email/password_subject_reset_mail.txt"
    email_template_name = 'users/email/password_reset_mail.html'
    extra_context = {"title": "Password Reset"}


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    """
    Представление установки нового пароля
    """
    form_class = UserSetNewPasswordForm
    template_name = 'users/registration/user_password_set_new.html'
    success_url = reverse_lazy('home:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Установить новый пароль'
        return context


class UserConfirmEmailView(View):
    """
    Активация аккаунта пользователя
    """
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = UserModel.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('users:email_confirmed')
        else:
            return redirect('users:email_confirmation_failed')


class EmailConfirmedView(TemplateView):
    """
    О успешном потверждение активации аккаунта
    """
    template_name = "users/registration/email_confirmed.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Вы актевировали свой аккаунт"
        return context


class EmailConfirmationFailedView(TemplateView):
    """
    О неуспешном потверждение активации аккаунта
    """
    template_name = "users/registration/email_confirmation_failed.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Вы не актевировали свой аккаунт"
        return context
