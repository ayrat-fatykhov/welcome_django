# Generated by Django 5.0.2 on 2024-03-19 18:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_blog_views_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.IntegerField(verbose_name='номер версии')),
                ('name', models.CharField(max_length=150, verbose_name='название версии')),
                ('is_active', models.BooleanField(default=True, verbose_name='признак текущей версии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
                'ordering': ('numbers',),
            },
        ),
    ]
