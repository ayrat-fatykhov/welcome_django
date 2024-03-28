from django.apps import AppConfig


class CatalogConfig(AppConfig):
    """
    Определяет пространственное имя для urls каталога
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'
