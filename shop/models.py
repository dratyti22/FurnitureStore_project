from django.db import models
from django.urls import reverse

from users.models import User


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Имя")
    slug = models.SlugField(max_length=200, unique=True,
                            blank=True, null=True, verbose_name="URL")

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.name


class Subcategories(models.Model):
    category = models.ForeignKey(
        to=Categories, on_delete=models.CASCADE, verbose_name="Категория")
    name = models.CharField(max_length=150, unique=True, verbose_name="Имя")
    slug = models.SlugField(max_length=200, unique=True,
                            blank=True, null=True, verbose_name="URL")

    class Meta:
        db_table = "subcategory"
        verbose_name = "Под категорию"
        verbose_name_plural = "Под категории"

    def __str__(self) -> str:
        return self.name


class Brends(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Имя")
    slug = models.SlugField(max_length=200, unique=True,
                            blank=True, null=True, verbose_name="URL")

    class Meta:
        db_table = "brend"
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"
    
    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(
        to=Categories, on_delete=models.CASCADE, verbose_name="Категория")
    subcategory = models.ForeignKey(
        to=Subcategories, on_delete=models.CASCADE, verbose_name="Под категория")
    brend = models.ForeignKey(
        to=Brends, on_delete=models.CASCADE, verbose_name="Бренд", blank=True, null=True)

    name = models.CharField(max_length=150, unique=True, verbose_name="Имя")
    slug = models.SlugField(max_length=200, unique=True,
                            blank=True, null=True, verbose_name="URL")
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание")

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("id",)
    
    def __str__(self):
        return self.name


class ProductImages(models.Model):
    product = models.ForeignKey(
        to=Products, on_delete=models.CASCADE, related_name="product_images", verbose_name="Товар")
    image = models.ImageField(upload_to='products',
                              blank=True, null=True, verbose_name="Изображение")

    class Meta:
        db_table = "product_image"
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return f"{self.product.name} - " + str(self.product.pk)


class ColorProducts(models.Model):
    product = models.ForeignKey(
        to=Products, on_delete=models.CASCADE, related_name="color_product", verbose_name="Товар")
    color = models.CharField(max_length=50, verbose_name="Цвет")

    class Meta:
        db_table = "color_product"
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"

    def __str__(self):
        return f"{self.product} | {self.color}"


class SizeProducts(models.Model):
    product = models.ForeignKey(
        to=Products, on_delete=models.CASCADE, related_name="size_product", verbose_name="Товар")
    color_product = models.ForeignKey(
        to=ColorProducts, on_delete=models.CASCADE, related_name="size_product", verbose_name="Товар")
    size = models.CharField(max_length=10, verbose_name="Размер")
    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена")
    discout = models.DecimalField(
        default=0.00, max_digits=4, decimal_places=2, verbose_name="Скидка в %")
    quantity = models.PositiveIntegerField(
        default=0, verbose_name="Количество")

    class Meta:
        db_table = "size_product"
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"

    def __str__(self):
        return f"{self.product} | {self.size} | {self.price}"

    def display_id(self):
        return f'{self.id:05}'

    # def get_absolute_url(self):
    #     return reverse("catalog:product", kwargs={"product_slug": self.slug})

    def sell_price(self):
        if self.discout:
            return round(self.price - self.price * self.discout / 100, 2)

        return self.price


class LikesProduct(models.Model):
    product = models.ForeignKey(
        to=Products, on_delete=models.CASCADE, verbose_name="Товар")
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, verbose_name="Товар")
    
    like = models.PositiveIntegerField(
        default=0, verbose_name="Нравится товар")
    
    class Meta:
        db_table = "like_product"
        verbose_name = "Нравится товар"
        verbose_name_plural = "Нраватся товары"

    def __str__(self):
        return f"{self.product} | {self.user} | {self.like}"
