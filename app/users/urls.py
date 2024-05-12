from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path("register/", views.UserRegisterView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path("account/", views.UserAccountView.as_view(), name="account"),
    path("address/", views.UserAddressView.as_view(), name="address"),
    path('password-reset/', views.UserForgotPasswordView.as_view(),
         name='password_reset'),
    path('set-new-password/<uidb64>/<token>/',
         views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('confirm-email/<str:uidb64>/<str:token>/',
         views.UserConfirmEmailView.as_view(), name='confirm_email'),
    path('email-confirmed/', views.EmailConfirmedView.as_view(),
         name='email_confirmed'),
    path('confirm-email-failed/', views.EmailConfirmationFailedView.as_view(),
         name='email_confirmation_failed'),
    path("subscribe/", views.UserMailingListView.as_view(), name="subscribe"),
    path("subscribe_newsletter/", views.UserMailingCreateView.as_view(),
         name="subscribe_newsletter"),
]
