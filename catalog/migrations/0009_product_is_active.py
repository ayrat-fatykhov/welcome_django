# Generated by Django 4.2.11 on 2024-04-02 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_product_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='статус публикации'),
        ),
    ]
