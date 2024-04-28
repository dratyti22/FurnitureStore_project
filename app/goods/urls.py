from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("shop/", views.ShopListView.as_view(), name="shop"),
]
