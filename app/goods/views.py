from typing import Any
from django.db.models import Q, Max
from django.views.generic import ListView

from app.goods.utils import q_search


from .models import Product


class ShopListView(ListView):
    model = Product
    template_name = "goods/shop.html"
    context_object_name = "product"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Shop"
        return context

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset


class ShopResultView(ListView):
    model = Product
    template_name = "goods/shop.html"
    context_object_name = "product"
    paginate_by = 12
    allow_empty = True

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Search"
        return context

    def get_queryset(self):
        result = self.model.objects.all()

        search = self.request.GET.get('q', None)
        min_price = self.request.GET.get("min_price", None)
        max_price = self.request.GET.get("max_price", None)
        order_by = self.request.GET.get("order_by", None)

        if search:
            result = q_search(search)

        if min_price or max_price:
            result = result.exclude(
                Q(price__lte=min_price) | Q(price__gte=max_price))
        if order_by and order_by != 'default':
            result = result.order_by(order_by)

        return result
