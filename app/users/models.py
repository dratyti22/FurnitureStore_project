from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    icon = models.ImageField(upload_to="user_images",
                             verbose_name="Аватар",
                             blank=True,
                             validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))])
    address = models.TextField(verbose_name="Адрес", default="напишите адрес")

    class Meta:
        db_table = "app_users"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return self.username
