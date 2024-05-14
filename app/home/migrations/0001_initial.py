# Generated by Django 4.2.11 on 2024-05-13 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки обращения')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратная связь',
                'db_table': 'app_feedback',
                'ordering': ['-time_create'],
            },
        ),
    ]
