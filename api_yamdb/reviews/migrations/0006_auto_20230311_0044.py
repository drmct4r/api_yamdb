# Generated by Django 3.2 on 2023-03-10 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_alter_title_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genretitle',
            options={'ordering': ['id'], 'verbose_name': 'Соответствие жанра и произведения', 'verbose_name_plural': 'Таблица соответствия жанров и произведений'},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ['id'], 'verbose_name': ('Произведение',), 'verbose_name_plural': ('Произведения',)},
        ),
    ]