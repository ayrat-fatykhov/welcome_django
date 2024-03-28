from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    """
    Кастомная команда для заполнения базы данных
    """
    def handle(self, *args, **options):

        Category.objects.all().delete()

        category_list = [
            {'name': 'Телефон', 'description': 'Устройство для звонков'},
            {'name': 'Смартфон', 'description': 'Умный телефон'},
            {'name': 'Ноутбук', 'description': 'Мобильный компьютер'}
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        Category.objects.bulk_create(category_for_create)

        product_list = [
            {'name': 'Asus Zenphone 10',
             'description': 'Компактный смартфон',
             'category': Category.objects.get(name='Смартфон'),
             'price': 45000}
        ]

        product_for_create = []
        for product_item in product_list:
            product_for_create.append(Product(**product_item))

        Product.objects.bulk_create(product_for_create)
