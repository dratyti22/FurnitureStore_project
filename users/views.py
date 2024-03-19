from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import auth
from django.urls import reverse

from .forms import UserRegistrationForm, UserLoginForm


def registration(request):
    if request.method == 'POST':

        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegistrationForm()

    context = {
        'title': "Furea - Регистрация",
        "language": True,
        "currency": False,
        'form': form,
    }
    return render(request, 'users/register.html', context)


def login(request):
    if request.method == 'POST':
        formlog = UserLoginForm(data=request.POST)
        if formlog.is_valid():
            email = formlog.cleaned_data['email']
            password = formlog.cleaned_data['password']
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect(reverse("main:index"))
    else:
        formlog = UserLoginForm()
    context = {
        'title': "Furea - Авторизация",
        "language": True,
        "currency": False,
        'formlog': formlog,
    }
    return render(request, 'users/login.html', context)
