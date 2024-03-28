from django.contrib.auth.forms import UserCreationForm, PasswordResetForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    """
    Переопределяет заполняемые поля на странице регистрации нового пользователя
    """

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class UserPasswordRecoveryForm(PasswordResetForm):
    """
    Переопределяет заполняемые поля для восстановления пароля пользователя
    """

    class Meta:
        model = User
        fields = ('email',)
