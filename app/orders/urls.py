from django.urls import path

from . import views

app_name = "order"

urlpatterns = [
    path("order", views.create_order, name="order")
]

