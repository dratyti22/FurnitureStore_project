from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path("register/", views.UserRegisterView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path("account/", views.UserAccountView.as_view(), name="account"),
]
