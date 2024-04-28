from django.db.models import Min
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .models import ColorProduct, ImageProduct, SizeProduct


class ShopListView(ListView):
    model = SizeProduct
    template_name = "goods/shop.html"
    context_object_name = "products"
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Shop"
        # context["products"] = SizeProduct.objects.all()
        return context

    # def get_queryset(self):
    #     queryset = SizeProduct.objects.all().annotate(
    #         min_size_product=Min('size')
    #     )
    #     product_list = []
    #     for i in queryset:
    #         if i.min_size_product:
    #             if i.min_size_product.discount:
    #                 product_list.append(i.min_size_product)
    #                 break
    #         else:
    #             product_list.append(i)
    #     if not product_list:
    #         product_list.append(get_object_or_404(SizeProduct, discount=None))
    #     return product_list[:1]
