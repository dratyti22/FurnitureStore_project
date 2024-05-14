from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("shop/", views.ShopListView.as_view(), name="shop"),
    path("search/", views.ShopResultView.as_view(), name="search"),
    path("filter/", views.ShopResultView.as_view(), name="filter"),
    path("detail/<int:pk>/", views.ProductDeteilView.as_view(), name="product_detail"),
    path("detail/<int:pk>/comment_create_view/", views.CommentCreateView.as_view(), name="comment_create_view"),
]
