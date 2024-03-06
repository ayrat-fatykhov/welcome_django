from django.contrib import admin

from catalog.models import Product, Category, Blog


# admin.site.register(Category)
# admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_price', 'product_category',)
    list_filter = ('product_category',)
    search_fields = ('product_name', 'product_description',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title',)
