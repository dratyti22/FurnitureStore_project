from django.db import models


class StocksIndex(models.Model):

    above_text = models.CharField(max_length=200,
                                  blank=True, null=True, verbose_name="Текст сверху над зоголовком")
    text = models.CharField(max_length=155, verbose_name="Текст акции")
    description_text = models.CharField(
        max_length=250, verbose_name="Описание акции")
    text_button = models.CharField(max_length=50, verbose_name="Текст кнопки")
    image = models.ImageField(upload_to='index_images',
                              verbose_name="Изображение")

    class Meta:
        db_table = 'stocks_index'
        verbose_name = 'Название акции'
        verbose_name_plural = 'Названия акции'

    def __str__(self):
        return self.text


class BannerIndex(models.Model):
    text = models.CharField(max_length=100, verbose_name='Текст')
    image = models.ImageField(upload_to='index_images/banners',
                              verbose_name="Изображение")

    class Meta:
        db_table = 'banner_index'
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'


class Product(models.Model):
    ...  # булет в goods для продуктов


class PopularItemsTitle(models.Model):
    text = models.CharField(
        max_length=150, verbose_name='Название популярных товаров')

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'popular_items_title'
        verbose_name = 'Название популярных товаров'
        verbose_name_plural = 'Названия популярных товаров'


class PopularItems(models.Model):
    category = models.CharField(max_length=80, verbose_name='Категория')

    def __str__(self):
        return self.category

    class Meta:
        db_table = 'popular_items'
        verbose_name = 'Популярный товар'
        verbose_name_plural = 'Популярные товары'


class PopularItemsProduct(models.Model):
    item = models.ForeignKey(
        to=PopularItems, on_delete=models.CASCADE, verbose_name='Категория товаров')
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity_page = models.PositiveIntegerField(
        default=0, verbose_name='Количество товара на 1 категории')

    class Meta:
        db_table = 'popular_items_product'
        verbose_name = 'Популярный товар'
        verbose_name_plural = 'Популярные товары'
