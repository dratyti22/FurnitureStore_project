from decimal import Decimal
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class CategoryModel(MPTTModel):
    name = models.CharField(max_length=255, verbose_name="Категория")
    slug = models.SlugField(max_length=255, verbose_name="URL категории")
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
        verbose_name="Родительская категория",
    )

    class MPTTMeta:
        order_insertion_by = ('name',)

    class Meta:
        ordering = ("name",)
        indexes = [models.Index(fields=["name"])]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'app_categories'

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(
        to=CategoryModel, related_name="product", on_delete=models.PROTECT)
    name = models.CharField(max_length=255, verbose_name="Название продукта")
    slug = models.SlugField(max_length=255, verbose_name="URL продукта")
    description = models.TextField(verbose_name="Описание")

    color = models.CharField(max_length=255, verbose_name="Цвет")

    size = models.PositiveIntegerField(verbose_name="Размер")

    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена")
    discount = models.DecimalField(
        default=0.00, max_digits=4, decimal_places=2, verbose_name="Скидка в %")
    quantity = models.PositiveIntegerField(
        default=0, verbose_name="Количество")

    image = models.ImageField(
        upload_to="product_images", verbose_name="Фото", null=True, blank=True)

    class Meta:
        ordering = ("id", "name", "price")
        indexes = [models.Index(fields=["name", "description"])]
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        db_table = 'app_product'

    def __str__(self) -> str:
        return self.name

    def sell_price(self):
        if self.discount:
            return Decimal(self.price - self.price * self.discount / 100).quantize(Decimal('0.01'))

        return self.price
