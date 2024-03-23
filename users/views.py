from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from main.models import SocialNetwork
from users.models import User

from .forms import UserAccountAdressForm, UserRegistrationForm, UserLoginForm


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
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main:index"))
    else:
        formlog = UserLoginForm()

    context = {
        'title': "Furea - Авторизация",
        "language": True,
        "currency": False,
        'formlog': formlog,
    }
    return render(request, 'users/login.html', context)


@login_required
def account(request):
    if request.method == 'POST':
        form = UserAccountAdressForm(data=request.POST)
        if form.is_valid():
            user = request.user
            addres = form.cleaned_data['addres']
            user.addres = addres
            user.save()
            return redirect(reverse("users:account"))
    else:
        form = UserAccountAdressForm()

    social_network = SocialNetwork.objects.all()
    user = User.objects.get(username=request.user.username)
    context = {
        'title': "Furea - Профиль",
        "language": True,
        "currency": False,
        'social_network': social_network,
        'username': request.user.username,
        'user': user,
        'form': form,  # Передаем форму в контекст шаблона
    }
    return render(request, 'users/account.html', context)


def delete_address(request):
    if request.method == 'DELETE':
        user = request.user
        user.addres = None
        user.save()
        return JsonResponse({'message': 'Address successfully deleted!'})
    else:
        return JsonResponse({'error': 'Invalid request method'})


def logout(request):
    auth.logout(request)
    return redirect(reverse("main:index"))
