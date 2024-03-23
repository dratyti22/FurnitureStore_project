from django.contrib import admin

from .models import Categories, ColorProducts, LikesProduct, SizeProducts, Subcategories, Brends, Products, ProductImages


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')


@admin.register(Subcategories)
class SubcategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('category', 'name', 'slug')


@admin.register(Brends)
class BrendsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'brend', 'subcategory', 'category')
    search_fields = ["name", "description"]
    list_filter = ['category', 'subcategory', 'brend']


@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('product',)


@admin.register(ColorProducts)
class ColorProductsAdmin(admin.ModelAdmin):
    list_display = ('product', 'color')


@admin.register(SizeProducts)
class SizeProductsAdmin(admin.ModelAdmin):
    list_display = ('product', 'color_product', 'size', 'quantity', 'discout')
    list_editable = ['quantity', 'discout']
    search_fields = ['product', 'color_product', 'size']
    list_filter = ['product', 'color_product', 'size', 'quantity', 'price']


@admin.register(LikesProduct)
class LikesProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'like')
