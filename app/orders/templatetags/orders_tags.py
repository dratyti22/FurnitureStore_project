from django import template

from ..utils import get_total_price, get_product

register = template.Library()


@register.simple_tag
def get_total_price_order(request):
    return get_total_price(request)


@register.simple_tag
def get_product_for_cart(request):
    return get_product(request)
