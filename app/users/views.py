from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from .forms import UserRegisterForm


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
