# Generated by Django 4.2.11 on 2024-04-02 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_version_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='признак текущей версии'),
        ),
    ]
