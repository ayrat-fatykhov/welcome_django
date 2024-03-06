from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='наименование категории')
    category_description = models.TextField(verbose_name='описание категории')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('category_name',)


class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='наименование продукта')
    product_description = models.TextField(verbose_name='описание продукта')
    product_image = models.ImageField(upload_to='product/', verbose_name='изображение продукта', **NULLABLE)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория продукта')
    product_price = models.IntegerField(verbose_name='цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата изменения')

    def __str__(self):
        return f'{self.product_name} {self.product_price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_name',)


class Blog(models.Model):
    blog_title = models.CharField(max_length=100, verbose_name='заголовок блога')
    blog_slug = models.CharField(max_length=150, verbose_name='blog_slug', **NULLABLE)
    blog_content = models.TextField(verbose_name='содержимое блога')
    blog_preview = models.ImageField(upload_to='blog/', verbose_name='превью блога', **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    is_publication = models.BooleanField(default=True, verbose_name='признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f'{self.blog_title}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ('created_at',)
