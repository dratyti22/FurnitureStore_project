# Generated by Django 4.2.11 on 2024-05-06 14:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Время добавления'),
            preserve_default=False,
        ),
    ]
