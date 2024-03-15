from django.contrib import admin

from main.models import PopularItems, PopularItemsProduct, PopularItemsTitle, StocksIndex, BannerIndex


@admin.register(StocksIndex)
class StocksIndexAdmin(admin.ModelAdmin):
    # Include all fields you want to display/edit
    list_display = ('above_text', 'text', 'description_text')
    # Make all the fields editable
    list_editable = ['text']
    # Specify which field to link in the list display


@admin.register(BannerIndex)
class BannerIndexAdmin(admin.ModelAdmin):
    list_display = ['text']


@admin.register(PopularItemsTitle)
class PopularItemsTitleAdmin(admin.ModelAdmin):
    list_display = ['text']


@admin.register(PopularItems)
class PopularItemsAdmin(admin.ModelAdmin):
    list_display = ['category']  # Change 'title' to 'category'


@admin.register(PopularItemsProduct)
class PopularItemsProductAdmin(admin.ModelAdmin):
    list_display = ['item', 'product', 'quantity_page']
