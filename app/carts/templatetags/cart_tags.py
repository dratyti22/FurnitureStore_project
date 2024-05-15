from django import template

from ..utils import get_user_carts, get_user_wishlist

register = template.Library()

@register.simple_tag
def user_carts(request):
    return get_user_carts(request)

@register.simple_tag
def user_wishlist(request):
    return get_user_wishlist(request)
