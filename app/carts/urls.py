from django.urls import path

from . import views

app_name="carts"

urlpatterns = [
    path("add_cart/", views.add_cart, name="add_cart")
]

