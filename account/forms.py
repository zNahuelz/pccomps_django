from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User,Product,Brand,Category

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","email")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username","email")

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'