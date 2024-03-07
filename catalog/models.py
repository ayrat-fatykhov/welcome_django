from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """
    Определяет поля для модели 'Категория'
    """
    name = models.CharField(max_length=150, verbose_name='наименование категории')
    description = models.TextField(verbose_name='описание категории')

    def __str__(self):
        """
        Показывает поля модели 'Категория' в админке
        """
        return f'{self.name}'

    class Meta:
        """
        Показывает в админке название модели в единственном и множеством числе, сортирует элементы по первичному ключу
        """
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('pk',)


class Product(models.Model):
    """
    Определяет поля для модели 'Продукт'
    """
    name = models.CharField(max_length=150, verbose_name='наименование продукта')
    description = models.TextField(verbose_name='описание продукта')
    image = models.ImageField(upload_to='product/', verbose_name='изображение продукта', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория продукта')
    price = models.IntegerField(verbose_name='цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата изменения')

    def __str__(self):
        """
        Показывает поля модели 'Продукт' в админке
        """
        return f'{self.name} {self.price}'

    class Meta:
        """
        Показывает в админке название модели в единственном и множеством числе, сортирует элементы по первичному ключу
        """
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('pk',)


class Blog(models.Model):
    """
    Определяет поля для модели 'Блог'
    """
    title = models.CharField(max_length=100, verbose_name='заголовок блога')
    slug = models.CharField(max_length=150, verbose_name='blog_slug', **NULLABLE)
    content = models.TextField(verbose_name='содержимое блога')
    preview = models.ImageField(upload_to='blog/', verbose_name='превью блога', **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    is_publication = models.BooleanField(default=True, verbose_name='признак публикации')
    views_count = models.PositiveIntegerField(default=0, verbose_name='просмотры', editable=False)

    def __str__(self):
        """
        Показывает поля модели 'Блог' в админке
        """
        return f'{self.title}'

    class Meta:
        """
        Показывает в админке название модели в единственном и множеством числе, сортирует элементы по первичному ключу
        """
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ('created_at',)
