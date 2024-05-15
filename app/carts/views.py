from typing import Any
from django.shortcuts import redirect, render
from django.views.generic import ListView

from app.carts.models import Cart, Wishlist
from app.carts.utils import get_user_carts
from app.goods.models import Product


def add_cart(request, pk):
    product = Product.objects.get(id=pk)

    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, product=product)

        if cart.exists():
            cart = cart.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    return redirect(request.META.get("HTTP_REFERER"))


def add_wishlist(request, pk):
    product = Product.objects.get(id=pk)

    Wishlist.objects.create(user=request.user, product=product,  quantity=1)

    return redirect(request.META.get("HTTP_REFERER"))

class WishlistListView(ListView):
    model = Wishlist
    template_name = "carts/wislist.html"
    context_object_name = "wishlist"
    queryset = model.objects.all()
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Wishlist"
        return context
    