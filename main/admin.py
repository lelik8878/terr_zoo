from django.contrib import admin

from .models import Brand, Category, Article, Product, Basket, Order, ProductType, Reviews, ProductProperties,OtherImage

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(Order)
admin.site.register(ProductType)
admin.site.register(Reviews)
admin.site.register(ProductProperties)
admin.site.register(OtherImage)

