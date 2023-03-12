# Generated by Django 3.2 on 2023-03-12 08:27

from django.db import migrations, models
import reviews.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_alter_title_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.IntegerField(db_index=True, validators=[reviews.validators.my_score_validator]),
        ),
    ]
