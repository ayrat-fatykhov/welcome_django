from django.contrib import admin

from catalog.models import Product, Category, Blog, Version


# admin.site.register(Category)
# admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Version)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('numbers', 'name', 'product', 'is_active',)