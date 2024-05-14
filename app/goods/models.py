from decimal import Decimal
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse


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


class Brands(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название бренда")
    slug = models.SlugField(max_length=255, verbose_name="URL бренда")

    class Meta:
        db_table = "app_brend"
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

    def __str__(self):
        return self.name


class Product(models.Model):

    class ProductManager(models.Manager):
        def all(self):
            return self.get_queryset().select_related("category",  "brand")

    brand = models.ForeignKey(
        to=Brands,  related_name="products", on_delete=models.PROTECT)
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

    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name='Время добавления')

    objects = ProductManager()

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

    def get_id(self):
        return f"{self.id:05}"

    def get_absolute_url(self):
        return reverse('catalog:product_detail', kwargs={'pk': self.pk})
    
    def save(self, *args, **kwargs):
        if not self.image:
            self.image = "media/default_product.png"
        super().save(*args, **kwargs)
