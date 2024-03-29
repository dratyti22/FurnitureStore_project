# Generated by Django 4.2.10 on 2024-03-23 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sizeproducts',
            name='like',
        ),
        migrations.AlterField(
            model_name='products',
            name='brend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.brends', verbose_name='Бренд'),
        ),
        migrations.CreateModel(
            name='LikesProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.PositiveIntegerField(default=0, verbose_name='Нравится товар')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.products', verbose_name='Товар')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Нравится товар',
                'verbose_name_plural': 'Нраватся товары',
                'db_table': 'like_product',
            },
        ),
    ]
