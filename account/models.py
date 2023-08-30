from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254,unique=True, null=False, blank=False)
    address = models.CharField(max_length=180, null=True, blank=True, unique=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True, unique=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    class Meta(AbstractUser.Meta):
       swappable = 'AUTH_USER_MODEL'

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table = "Categories"

class Brand(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    class Meta:
        db_table = "Brands"

class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT,
        blank = False
    )
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, blank=False 
    )
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    stock = models.IntegerField(null=False, blank=False, default=0)
    buy_price = models.DecimalField(null=False, blank=False, default=0.0, decimal_places=2, max_digits=8)
    sell_price = models.DecimalField(null=False, blank=False, default=0.0,decimal_places=2, max_digits=8)
    is_active = models.BooleanField(default=True)
    image = models.CharField(max_length=255, null=False, blank= True)
    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table = "Products"