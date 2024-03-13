from django.contrib import admin

from main.models import StocksIndex, BannerIndex


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
