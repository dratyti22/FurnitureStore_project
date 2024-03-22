from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('account/', views.account, name='account'),
    path('logout/', views.logout, name='logout'),
    path('delete_address/', views.delete_address, name='delete_address'),
]
