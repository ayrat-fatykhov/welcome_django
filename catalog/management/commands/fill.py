from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):

        Category.objects.all().delete()

        category_list = [
            {'category_name': 'Телефон', 'category_description': 'Устройство для звонков'},
            {'category_name': 'Смартфон', 'category_description': 'Умный телефон'},
            {'category_name': 'Ноутбук', 'category_description': 'Мобильный компьютер'}
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        Category.objects.bulk_create(category_for_create)

        product_list = [
            {'product_name': 'Asus Zenphone 10',
             'product_description': 'Компактный смартфон',
             'product_category': Category.objects.get(category_name='Смартфон'),
             'product_price': 45000}
        ]

        product_for_create = []
        for product_item in product_list:
            product_for_create.append(Product(**product_item))

        Product.objects.bulk_create(product_for_create)
