from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin
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


class UserIsNotOrdinary(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not (request.user.is_staff or request.user.is_superuser):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
