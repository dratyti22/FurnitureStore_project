from django.contrib import admin

from .models import UserModel, EmailMailingList

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active', 'is_staff', 'is_superuser')

@admin.register(EmailMailingList)
class AdminEmailMailingList(admin.ModelAdmin):
    list_display = ["user_display", "email"]

    def user_display(self, obj):
        if obj.user:
            return obj.user.username
