from django.db import models

from app.users.models import UserModel


class Feedback(models.Model):
    user = models.ForeignKey(to=UserModel, verbose_name='Пользователь',
                             on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    phone_number = models.CharField(
        max_length=15, verbose_name="Номер телефона")
    email = models.EmailField(max_length=255, verbose_name="Email")
    message = models.TextField(verbose_name="Сообщение")
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата отправки обращения')

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['-time_create']
        db_table = 'app_feedback'

    def __str__(self):
        return f"Вам письмо от {self.email}"
