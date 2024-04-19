# Generated by Django 4.2.11 on 2024-04-19 07:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='icon',
            field=models.ImageField(blank=True, default=1, upload_to='user_images', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))], verbose_name='Аватар'),
            preserve_default=False,
        ),
    ]