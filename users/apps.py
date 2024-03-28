from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    Определяет пространственное имя для urls пользователя
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
