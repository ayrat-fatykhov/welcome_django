# Generated by Django 5.0.2 on 2024-03-07 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_blog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('pk',), 'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('pk',), 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='blog_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='blog_preview',
            new_name='preview',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='blog_slug',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='blog_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='category_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_price',
            new_name='price',
        ),
    ]
