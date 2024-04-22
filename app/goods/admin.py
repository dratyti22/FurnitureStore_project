from django.contrib import admin

from .models import CategoryModel, Product, SizeProduct, ColorProduct, ImageProduct
from mptt.admin import DraggableMPTTAdmin


@admin.register(CategoryModel)
class CategoryModelAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'id', 'name', 'slug')
    list_display_links = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

    fieldsets = (
        ('Основная информация', {'fields': ('name', 'slug', 'parent')}),
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(ColorProduct)
class ColorProductAdmin(admin.ModelAdmin):
    list_display = ("color",)
    prepopulated_fields = {"slug": ("color",)}


@admin.register(SizeProduct)
class SizeProductAdmin(admin.ModelAdmin):
    list_display = ("size", "price", "quantity", "discount", "slug")
    list_editable = ("price", "discount", "quantity")
    prepopulated_fields = {"slug": ("size",)}


@admin.register(ImageProduct)
class ImageProductAdmin(admin.ModelAdmin):
    list_display = ('color', "image")
