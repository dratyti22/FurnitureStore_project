from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


class UserIsNotAuth(UserPassesTestMixin):
    """
    Проверка авторизации аккаунта
    """
    def test_func(self) -> bool | None:
        if self.request.user.is_authenticated:
            raise PermissionDenied
        return True

    def handle_no_permission(self):
        return redirect('home:home')
