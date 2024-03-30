from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """
    Определяет поля для модели 'Пользватель'
    """
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='страна', **NULLABLE)

    ver_code = models.CharField(verbose_name='код верификации', **NULLABLE)

    """
    Реализуют возможность взаимодействия с пользователем через email
    (по умолчанию установлено поле 'имя пользователя')
    """

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
