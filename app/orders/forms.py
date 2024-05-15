from django import forms

from app.orders.models import Order


class OrderForm(forms.Form):
    class Meta:
        model = Order
        fields = ("phone", "first_name", 'last_name',
                  'code', 'order_notes', 'adress', 'town_city', 'postal_code')
