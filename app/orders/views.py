from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db import transaction

from app.carts.models import Cart
from app.orders.forms import OrderForm
from app.orders.models import Order


@login_required
def create_order(request):
    if request.method == "POST":
        form = OrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)
                    if cart_items.exists():
                        Order.objects.create(
                            user=user,
                            phone=form.cleaned_data.get("phone"),
                            code=form.cleaned_data.get('code'),
                            first_name=form.cleaned_data.get('first_name'),
                            last_name=form.cleaned_data.get('last_name'),
                            order_notes=form.cleaned_data.get('order_notes'),
                            adress=form.cleaned_data.get('adress'),
                            town_city=form.cleaned_data.get('town_city'),
                        )
                        # Создать заказанные товары
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.sell_price()
                            quantity = cart_item.quantity

                            if product.quantity < quantity:
                                raise ValidationError(f'Недостаточное количество товара {name} на складе\
                                                       В наличии - {product.quantity}')

                            product.quantity -= quantity
                            product.save()
                        cart_items.delete()
                        return redirect("home:home")

            except ValidationError as e:
                return redirect('home:home')

    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }

        form = OrderForm(initial=initial)

    context = {
        'title': "Home = Оформление заказа",
        "form": form,
    }

    return render(request, 'orders/checkout.html', context=context)
