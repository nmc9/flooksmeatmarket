from django.contrib import admin

# Register your models here.
from .models import Product, Basket, OrderLine

admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(OrderLine)