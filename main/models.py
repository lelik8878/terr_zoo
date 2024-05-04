from django.contrib.auth.models import User
from django.db import models


class Brand(models.Model):
    brand_name = models.CharField(max_length=256, verbose_name='Название')
    brand_logo = models.ImageField(upload_to='media', verbose_name='Логотип')
    brand_description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Брэнд'
        verbose_name_plural = 'Брэнды'

    def __str__(self):
        return self.brand_name


class Category(models.Model):
    category_name = models.CharField(max_length=256, verbose_name='Название категории')
    category_name_plural = models.CharField(max_length=256, verbose_name='Множ_чис_род_пажеж')
    category_image = models.ImageField(upload_to='media', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name


class ProductType(models.Model):
    type_of_product = models.CharField(max_length=256, verbose_name='Тип товара')

    class Meta:
        verbose_name = 'Тип товаров'
        verbose_name_plural = 'Типы товаров'

    def __str__(self):
        return self.type_of_product


class Article(models.Model):
    article_name = models.CharField(max_length=256, verbose_name='Название статьи')
    image = models.ImageField(upload_to='media', verbose_name='Изображение')
    item = models.TextField(verbose_name='Текст статьи')
    pub_date = models.DateField(verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.article_name


class Product(models.Model):
    product_name = models.CharField(max_length=256, verbose_name='Название товара')
    product_type = models.ForeignKey('ProductType', on_delete=models.CASCADE, verbose_name='Тип товара')
    manufacturer = models.ForeignKey('Brand', on_delete=models.CASCADE, verbose_name='Производитель')
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    product_image = models.ImageField(upload_to='media', verbose_name='Изображение')
    other_images = models.ForeignKey('OtherImage', on_delete=models.CASCADE, blank=True,
                                     null=True, verbose_name='Другие изображения')
    product_properties = models.ForeignKey('ProductProperties', on_delete=models.CASCADE, verbose_name='Свойства товара')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.product_name} --- {self.manufacturer}'


class ProductProperties(models.Model):
    weight = models.CharField(max_length=50, verbose_name='Вес')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    rating = models.IntegerField(verbose_name='Рейтинг')
    pub_date = models.DateTimeField(verbose_name='Дата добавления')

    class Meta:
        verbose_name = 'Свойства товара'
        verbose_name_plural = 'Свойства товаров'

    def __str__(self):
        return f'{self.weight} --- {self.price}'


class OtherImage(models.Model):
    product_image_1 = models.ImageField(upload_to='media', blank=True, null=True, verbose_name='Изображение 1')
    product_image_2 = models.ImageField(upload_to='media', blank=True, null=True, verbose_name='Изображение 2')
    product_image_3 = models.ImageField(upload_to='media', blank=True, null=True, verbose_name='Изображение 3')

    class Meta:
        verbose_name = 'Другая картинка'
        verbose_name_plural = 'Другие картинки'


class Basket(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')
    amount = models.IntegerField(verbose_name='Количество')
    cost = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Стоимость')
    is_complete = models.BooleanField(verbose_name='Подтвержден')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'{self.user_name} --- {self.product}'


class Order(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    user_voiced_name = models.CharField(max_length=56, verbose_name='Имя клиента')
    user_tel = models.CharField(max_length=10, verbose_name='Номер телефона')
    total_order_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Стоимость')
    order_compound = models.ForeignKey('Basket', on_delete=models.CASCADE, verbose_name='Позиции')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.user_name} --- {self.total_order_price}'


class Reviews(models.Model):
    user_name = models.CharField(max_length=56, verbose_name='Имя клиента')
    review_text = models.TextField(verbose_name='Текст отзыва')
    user_tel = models.IntegerField(verbose_name='Номер телефона')
    pet = models.CharField(max_length=56, verbose_name='Питомец')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.user_name} --- {self.pet}'
