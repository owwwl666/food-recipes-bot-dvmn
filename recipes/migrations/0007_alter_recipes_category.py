# Generated by Django 4.2.5 on 2023-09-22 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_remove_recipes_category_recipes_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='category',
            field=models.ManyToManyField(related_name='recipes', to='recipes.category', verbose_name='Категория'),
        ),
    ]