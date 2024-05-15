from app.carts.models import Cart


def get_total_price(request):
    return Cart.objects.total_price()

def get_product(request):
    return Cart.objects.all()
