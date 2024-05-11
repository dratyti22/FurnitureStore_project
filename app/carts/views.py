from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from app.carts.models import Cart
from app.carts.utils import get_user_carts
from app.goods.models import Product


def add_cart(request):
    product_id = request.POST.get("product_id")

    print(product_id)

    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, product=product)

        if cart.exists():
            cart = cart.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/shopping_cart.html"
    )
    response_data = {
        "cart_items_html": cart_items_html
    }

    return JsonResponse(response_data)