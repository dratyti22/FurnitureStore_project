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
