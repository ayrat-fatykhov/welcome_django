from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, UserPasswordRecoveryView, EmailConfirmView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('recovery/', UserPasswordRecoveryView.as_view(), name='recovery'),
    path('emailconfirm/', EmailConfirmView.as_view(), name='email_confirm'),
]
