# Generated by Django 3.2 on 2023-03-10 11:09

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_confirmation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='confirmation_code',
            field=models.UUIDField(default=uuid.UUID('4529d437-cbe7-4eab-a28b-b70c509f09c7'), verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=150, unique=True, validators=[django.core.validators.RegexValidator(message='Имя пользователя содержит недопустимый символ', regex='^[\\w.@+-]+$')], verbose_name='Никнейм'),
        ),
    ]