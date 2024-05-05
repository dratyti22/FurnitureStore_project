from django.contrib import admin

from .models import CategoryModel, Product, Brands
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
    list_display = ("name", "price", "discount", "quantity")
    list_editable = ("price", "discount", "quantity")
    list_filter = ("id", "name", "price", "discount", "quantity")
    prepopulated_fields = {'slug': ('name', "color", "size")}


@admin.register(Brands)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {'slug': ('name',)}
