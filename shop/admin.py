# shop/admin.py
from django.contrib import admin
from .models import Category, SubCategory, Product, CartItem, Order

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Order)