from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Кастомная команда для создания супер пользователя
    """

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@sky.pro',
            first_name='Admin',
            last_name='Skypro',
            is_superuser=True,
            is_staff=True,
        )

        user.set_password('123qwe567rty')
        user.save()
