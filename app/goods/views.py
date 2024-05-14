from typing import Any
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from app.goods.forms import CommentCreateForm
from app.goods.utils import q_search


from .models import Brands, Comment, Product


class ShopListView(ListView):
    """
    view для показывания товаров
    """
    model = Product
    template_name = "goods/shop.html"
    context_object_name = "product"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Shop"
        context["brands"] = Brands.objects.all()
        return context

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset


class ShopResultView(ShopListView):
    """
    Поиск и филтрация товаров
    """
    allow_empty = True

    def get_queryset(self):
        result = self.model.objects.all()

        search = self.request.GET.get('q', None)
        min_price = self.request.GET.get("min_price", None)
        max_price = self.request.GET.get("max_price", None)
        order_by = self.request.GET.get("order_by", None)
        brand = self.request.GET.get("brand", None)

        if search:
            result = q_search(search)

        if min_price or max_price:
            result = result.exclude(
                Q(price__lte=min_price) | Q(price__gte=max_price))
        if order_by and order_by != 'default':
            result = result.order_by(order_by)

        if brand:
            result = result.filter(brand__name=brand)

        return result


class ProductDeteilView(DetailView):
    model = Product
    template_name = "goods/product_details.html"
    context_object_name = "product_detail"
    queryset = model.objects.all()

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Product Detail"
        return context


class CommentCreateView(CreateView, LoginRequiredMixin):
    model = Comment
    form_class = CommentCreateForm

    def is_ajax(self):
        return self.request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    def form_invalid(self, form):
        if self.is_ajax():
            return JsonResponse({'error': form.errors}, status=400)
        return super().form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.name = self.request.POST.get('name')
        comment.message = self.request.POST.get('message')
        comment.email = self.request.POST.get('email')
        if self.is_ajax():
            return JsonResponse({
                'is_child': comment.is_child_node(),
                'id': comment.id,
                'name': comment.name,
                'parent_id': comment.parent_id,
                'time_create': comment.time_create.strftime('%Y-%b-%d %H:%M:%S'),
                'avatar': comment.user.icon.url,
                'message': comment.message,
            }, status=200)
        
        return redirect(comment.product.get_absolute_url()), super().form_valid(form)

    def handle_no_permission(self):
        return JsonResponse({'error': 'Необходимо авторизоваться для добавления комментариев'}, status=400)
