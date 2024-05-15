from django.urls import path

from . import views

app_name = "cart"

urlpatterns = [
    path("add_cart/<int:pk>/", views.add_cart, name="add_cart"),
    path("add_wishlist/<int:pk>/", views.add_wishlist, name="add_wishlist"),
    path("wishlist/", views.WishlistListView.as_view(), name="wishlist"),
]
