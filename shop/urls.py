from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path('shoping/', views.shoping, name='shoping'),
]
