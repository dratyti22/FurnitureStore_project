from django.db.models import Min
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .models import Product


class ShopListView(ListView):
    model = Product
    template_name = "goods/shop.html"
    context_object_name = "product"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Shop"
        return context

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset
