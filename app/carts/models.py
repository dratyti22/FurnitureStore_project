from django.db import models

from app.goods.models import Product
from app.users.models import UserModel


class CartQueryset(models.QuerySet):
    def total_price(self):
        return sum(item.products_price() for item in self)

    def total_quantity(self):
        result = sum(item.quantity for item in self)
        if result > 0:
            return result
        return 0


class Cart(models.Model):

    user = models.ForeignKey(to=UserModel,  on_delete=models.CASCADE,
                             blank=True, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, verbose_name="Продукт")
    quantity = models.PositiveSmallIntegerField(
        default=0, verbose_name="Количество")
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name='Время создания')

    objects = CartQueryset().as_manager()

    class Meta:
        db_table = "app_cart"
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self) -> str:
        if self.user:
            return f"Корзина: {self.user.username} | Товар: {self.product.name} | Количество: {self.quantity}"

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)


class Wishlist(models.Model):

    STATUS_OPTIONS = (
        ('in stock', 'в наличии'),
        ('It over', 'закончилось')
    )

    user = models.ForeignKey(to=UserModel,  on_delete=models.CASCADE,
                             blank=True, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, verbose_name="Продукт")
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name='Время создания')
    status = models.CharField(
        choices=STATUS_OPTIONS, default='in stock', verbose_name='Статус товара', max_length=15)
    quantity = models.PositiveSmallIntegerField(
        default=0, verbose_name="Количество")

    objects = CartQueryset().as_manager()

    class Meta:
        db_table = "app_wishlist"
        verbose_name = "Понравшийся товар"
        verbose_name_plural = "Понравшиеся товары"

    def __str__(self) -> str:
        if self.user:
            return f"Корзина: {self.user.username} | Товар: {self.product.name} | Количество: {self.quantity}"

    def save(self, *args, **kwargs):
        if self.product.quantity == 0:
            self.status = 'It over'
        super(Wishlist, self).save(*args, **kwargs)
