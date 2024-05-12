from django.contrib import admin

from .models import UserModel, EmailMailingList, EmailMailing


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active',
                    'is_staff', 'is_superuser')


@admin.register(EmailMailingList)
class AdminEmailMailingList(admin.ModelAdmin):
    list_display = ["user_display", "email"]

    def user_display(self, obj):
        if obj.user:
            return obj.user.username
        else:
            return "Незарегистрирован"


@admin.register(EmailMailing)
class AdminEmailMailing(admin.ModelAdmin):
    list_display = ["subject_display", "message_display", "time_sending"]

    def subject_display(self, obj):
        return f"{obj.subject[:20]}"

    def message_display(self, obj):
        return f"{obj.message[:20]}"
