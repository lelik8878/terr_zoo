# Generated by Django 5.0.2 on 2024-04-29 18:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='other_images',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.otherimage', verbose_name='Другие изображения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_properties',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productproperties', verbose_name='Свойства товара'),
        ),
    ]
