from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path("", views.HomeListView.as_view(), name="home"),
    path("contact/", views.Contact.as_view(), name="contact"),
]
