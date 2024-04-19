from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.files.base import ContentFile
import requests


class UserModel(AbstractUser):
    icon = models.ImageField(upload_to="user_images",
                             verbose_name="Аватар",
                             blank=True,
                             validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))])

    class Meta:
        db_table = "app_users"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return self.username
