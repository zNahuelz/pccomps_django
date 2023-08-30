from django.contrib import admin
from .models import User, Product, Brand, Category
# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)