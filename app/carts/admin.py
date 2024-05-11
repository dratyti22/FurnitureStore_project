from django.contrib import admin
from .models import Cart


@admin.register(Cart)
class AdminCart(admin.ModelAdmin):
    list_display = ["user_display", "product_display",
                    "quantity", "created_timestamp"]
    list_editable = ("quantity",)

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return 'Анонимный пользователь'

    def product_display(self, obj):

        return str(obj.product.name)
