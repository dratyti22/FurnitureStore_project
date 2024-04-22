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
    description = models.TextField(
        verbose_name="Описание")

    class Meta:
        ordering = ("name",)
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        db_table = 'app_product'

    def __str__(self) -> str:
        return self.name


class ColorProduct(models.Model):
    product = models.ForeignKey(
        to=Product, related_name="color", on_delete=models.CASCADE)
    color = models.CharField(max_length=255, verbose_name="Цвет")
    slug = models.SlugField(max_length=255, verbose_name="URL категории")
    image_color = models.ImageField(verbose_name="Фото цвета", blank=True, null=True, upload_to="image_color")

    class Meta:
        ordering = ("color",)
        indexes = [models.Index(fields=(["color"]))]
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"
        db_table = "app_product_color"

    def __str__(self):
        return f"{self.product.name}: {self.color}"


class SizeProduct(models.Model):
    color = models.ForeignKey(
        to=ColorProduct, related_name="size", on_delete=models.CASCADE)
    size = models.CharField(max_length=255, verbose_name="Размер")
    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена")
    discount = models.DecimalField(
        default=0.00, max_digits=4, decimal_places=2, verbose_name="Скидка в %")
    quantity = models.PositiveIntegerField(
        default=0, verbose_name="Количество")
    slug = models.SlugField(max_length=255, verbose_name="URL категории")

    class Meta:
        ordering = ["-size", "-price", "-discount"]
        indexes = [models.Index(fields=["-price", "-discount", "-quantity"])]
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"
        db_table = "app_product_size"

    def __str__(self):
        return f"{self.color.product.name}: {self.quantity}"

    def sell_price(self):
        if self.discount:
            return Decimal(self.price - self.price * self.discount / 100).quantize(Decimal('0.01'))

        return self.price

    def save(self, *args, **kwargs):
        self.slug = f"{self.color.product.name}-{self.color.color}-{self.size}"
        super().save(*args, **kwargs)


class ImageProduct(models.Model):
    color = models.ForeignKey(
        to=ColorProduct, related_name="image", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_images", verbose_name="Фото")

    class Meta:
        ordering = ("color", "image")
        indexes = [models.Index(fields=["color", "image"])]
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
        db_table = "app_product_image"

    def __str__(self):
        return self.color.product.name
