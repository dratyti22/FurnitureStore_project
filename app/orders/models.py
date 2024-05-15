from django.db import models

from app.carts.models import Cart
from app.goods.models import Product
from app.users.models import UserModel


class OrderitemQueryset(models.QuerySet):
    def total_price(self):
        return sum(item.products_price() for item in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Code(models.Model):
    code = models.CharField(max_length=100, verbose_name="Код скидки")
    discount = models.DecimalField(
        default=0.00, max_digits=4, decimal_places=2, verbose_name="Скидка в %")
    quantity = models.PositiveIntegerField(
        default=0, verbose_name="Количество")

    class Meta:
        db_table = 'app_code'
        verbose_name = "Код скидки"
        verbose_name_plural = "Коды скидки"

    def __str__(self):
        return f"Код: {self.code} | Скидка: {self.discount} | Количество: {self.quantity}"


class Order(models.Model):
    code = models.ForeignKey(to=Code, on_delete=models.CASCADE,
                             related_name="orders", verbose_name="Код скидки", null=True, blank=True)
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE,
                             related_name="orders", verbose_name="Пользователь", null=True, blank=True)
    cart = models.ForeignKey(
        to=Cart, on_delete=models.CASCADE, verbose_name="Корзина")

    phone = models.CharField(max_length=255, blank=True,
                             null=True, verbose_name="Номер телефона")
    first_name = models.CharField(max_length=200, verbose_name="Имя")
    last_name = models.CharField(max_length=200, verbose_name="Фамилия")
    order_notes = models.CharField(
        max_length=200, verbose_name="Примичания к заказу")
    adress = models.TextField(verbose_name="Адрес")
    town_city = models.CharField(
        max_length=255, verbose_name="Насиленный пункт или город")
    postal_code = models.PositiveIntegerField(verbose_name="Индекс страны")

    class Meta:
        db_table = "app_order"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ № {self.pk} | Покупатель {self.user.first_name} {self.user.last_name}"
