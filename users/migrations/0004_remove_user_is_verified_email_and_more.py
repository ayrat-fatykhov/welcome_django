# Generated by Django 4.2.11 on 2024-03-29 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_is_verified_email_emailverification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_verified_email',
        ),
        migrations.DeleteModel(
            name='EmailVerification',
        ),
    ]
