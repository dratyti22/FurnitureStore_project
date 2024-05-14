from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    icon = models.ImageField(upload_to="user_images",
                             verbose_name="Аватар",
                             blank=True,
                             validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))], 
                             default="media/user_images/default.jpg")
    address = models.TextField(verbose_name="Адрес", default="напишите адрес")

    class Meta:
        db_table = "app_users"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return self.username


class EmailMailingList(models.Model):
    """
    Модель пользователя, сохраянашая email для рассылки
    """
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE,
                             verbose_name="Пользователь", null=True, blank=True)
    email = models.EmailField(verbose_name="Email", unique=True)

    class Meta:
        db_table = "app_email_mailing_list"
        verbose_name = "Подписка на рассылку"
        verbose_name_plural = "Подписки на рассылку"

    def __str__(self):
        if self.user:
            return f"Подписка: {self.user.username} | Email: {self.email}"
        return self.email


class EmailMailing(models.Model):
    """
    Созранение письма рассылки
    """
    subject = models.CharField(max_length=200, verbose_name="Тема письма")
    message = models.TextField(verbose_name="Текст письма")
    img = models.ImageField(upload_to="email_mailing",
                            verbose_name="Фото",
                            null=True,
                            blank=True,
                            validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))])
    time_sending = models.DateTimeField(
        auto_now_add=True, verbose_name="Время отправки")

    class Meta:
        db_table = 'app_email_mailing'
        verbose_name = "Сохранение письма"
        verbose_name_plural = "Сохранение письм"

    def __str__(self):
        return f"{self.subject[:25]}"
