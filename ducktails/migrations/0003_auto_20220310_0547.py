# Generated by Django 3.1.4 on 2022-03-10 05:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ducktails', '0002_auto_20220310_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duckmodel',
            name='age',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(1)]),
        ),
    ]
