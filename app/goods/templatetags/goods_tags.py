from django.template import Library
from django.utils import timezone
from datetime import datetime, date, time, timedelta

from ..models import Product

register = Library()

@register.simple_tag
def get_time_product(id: int):
    # получаем текущую дату и время
    now = timezone.now()
    # вычисляем дату, которая была 7 дней назад
    start_date = now - timedelta(days=7)
    
    # Проверяем, что продукт был создан после start_date
    product = Product.objects.get(id=id)
    if product.time_create >= start_date:
        return True
    else:
        return False



