from .models import Cart, Wishlist


def get_user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user).select_related("product")


def get_user_wishlist(request):
    if request.user.is_authenticated:
        return Wishlist.objects.filter(user=request.user).select_related("product")
