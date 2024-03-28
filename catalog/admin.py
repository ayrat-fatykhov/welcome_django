from django.contrib import admin

from catalog.models import Product, Category, Blog, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Отображает в админке id и наименования категорий
    """
    list_display = ('id', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Отображает в админке id, наименования, цены и категорий продукта.
    Реализует возможности фильтрации продуктов по категориям и поиск продуктов по ключевому слову
    """
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """
    Отображает в админке заголовок блога
    """
    list_display = ('title',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    """
    Отображает в админке номер, наименование, продукт и активность версии
    """
    list_display = ('numbers', 'name', 'product', 'is_active',)