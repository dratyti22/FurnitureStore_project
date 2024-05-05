from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank

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


class ShopSearchResultView(ListView):
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
        query = self.request.GET.get('q')
        search_vector = SearchVector(
            'description', weight='B') + SearchVector('name', weight='A')
        search_query = SearchQuery(query)
        return (self.model.objects.annotate(rank=SearchRank(search_vector, search_query)).filter(rank__gte=0.5).order_by('-rank'))
