from django.contrib import admin
from django.urls import path

from .views import (get_home_page, get_main_page, register_user, log_in, log_out, get_user, get_catalog,
                    get_catalog_by_category, get_card_product, get_brands, get_articles, get_article_self,
                    get_basket, add_to_basket,get_increase, get_decrease, get_remove, get_card_increase,
                    get_card_decrease, get_order_create, get_order_complete, get_service, get_empty_basket)


urlpatterns = [
    path('', get_home_page, name='main'),
    path('home/', get_main_page, name='home'),
    path('register/', register_user, name='register'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('user/', get_user, name='user'),
    path('catalog/', get_catalog, name='catalog'),
    path('catalog/<int:category>/', get_catalog_by_category, name='catalog_by_category'),
    path('card_product/<int:product_id>/<int:product_amount>/', get_card_product, name='card_product'),
    path('brands/', get_brands, name='brands'),
    path('articles/', get_articles, name='articles'),
    path('articles/<str:article_name>/', get_article_self, name='article_self'),
    path('basket/', get_basket, name='basket'),
    path('add_to_basket/<int:product_id>/<int:product_amount>/', add_to_basket, name='add_basket'),
    path('increase/<int:product_id>/', get_increase, name='increase'),
    path('decrease/<int:product_id>/', get_decrease, name='decrease'),
    path('increase_card/<int:product_id>/<str:product_amount>/', get_card_increase, name='increase_card'),
    path('decrease_card/<int:product_id>/<str:product_amount>/', get_card_decrease, name='decrease_card'),
    path('remove/<int:product_id>/', get_remove, name='remove'),
    path('order_create/<str:total_price>/<int:total_amount>/', get_order_create, name='order_create'),
    path('order_complete/', get_order_complete, name='order_complete'),
    path('empty_basket/', get_empty_basket, name='empty_basket'),
    path('service/', get_service, name='service'),
]