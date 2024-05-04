# Generated by Django 5.0.2 on 2024-04-29 17:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_name', models.CharField(max_length=256, verbose_name='Название статьи')),
                ('image', models.ImageField(upload_to='media', verbose_name='Изображение')),
                ('item', models.TextField(verbose_name='Текст статьи')),
                ('pub_date', models.DateField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=256, verbose_name='Название')),
                ('brand_logo', models.ImageField(upload_to='media', verbose_name='Логотип')),
                ('brand_description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Брэнд',
                'verbose_name_plural': 'Брэнды',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=256, verbose_name='Название категории')),
                ('category_name_plural', models.CharField(max_length=256, verbose_name='Множ_чис_род_пажеж')),
                ('category_image', models.ImageField(upload_to='media', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='OtherImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image_1', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Изображение 1')),
                ('product_image_2', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Изображение 2')),
                ('product_image_3', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Изображение 3')),
            ],
            options={
                'verbose_name': 'Другая картинка',
                'verbose_name_plural': 'Другие картинки',
            },
        ),
        migrations.CreateModel(
            name='ProductProperties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.CharField(blank=True, max_length=50, null=True, verbose_name='Вес')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('rating', models.IntegerField(verbose_name='Рейтинг')),
                ('pub_date', models.DateTimeField(verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name': 'Свойства товара',
                'verbose_name_plural': 'Свойства товаров',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_product', models.CharField(max_length=256, verbose_name='Тип товара')),
            ],
            options={
                'verbose_name': 'Тип товаров',
                'verbose_name_plural': 'Типы товаров',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=56, verbose_name='Имя клиента')),
                ('review_text', models.TextField(verbose_name='Текст отзыва')),
                ('user_tel', models.IntegerField(verbose_name='Номер телефона')),
                ('pet', models.CharField(max_length=56, verbose_name='Питомец')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='Количество')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость')),
                ('is_complete', models.BooleanField(verbose_name='Подтвержден')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_voiced_name', models.CharField(max_length=56, verbose_name='Имя клиента')),
                ('user_tel', models.CharField(max_length=10, verbose_name='Номер телефона')),
                ('total_order_price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('order_compound', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.basket', verbose_name='Позиции')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=256, verbose_name='Название товара')),
                ('product_image', models.ImageField(upload_to='media', verbose_name='Изображение')),
                ('description', models.TextField(verbose_name='Описание')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.brand', verbose_name='Производитель')),
                ('other_images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.otherimage')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Категория')),
                ('product_properties', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productproperties')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.producttype', verbose_name='Тип товара')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.AddField(
            model_name='basket',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product', verbose_name='Продукт'),
        ),
    ]
