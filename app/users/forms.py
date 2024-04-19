from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserModel


class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = UserModel
        fields = UserCreationForm.Meta.fields + \
            ('email',)

    def clean_email(self):
        """
        Проверка email на уникальность
        """
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and UserModel.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(
                'Такой email уже используется в системе')
        return email


class UserLoginForm(AuthenticationForm):
    """
    Форма для аутификации пользователя
    """
    class Meta:
        model = UserModel
