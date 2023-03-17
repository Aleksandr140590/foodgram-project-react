# Generated by Django 3.2 on 2023-03-17 15:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'verbose_name': 'Ингредиент', 'verbose_name_plural': 'Ингредиенты'},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'verbose_name': 'Рецепт', 'verbose_name_plural': 'Рецепты'},
        ),
        migrations.AlterField(
            model_name='ingredienttorecipe',
            name='amount',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(1, 'Количество должно быть целым числом более 1')]),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, 'Время приготовления не может быть менее 1 минуты')], verbose_name='Время приготовления, мин'),
        ),
    ]