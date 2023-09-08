# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.shortcuts import render,redirect
from .models import Product,Brand,Category

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def Dashboard(request):
    if request.user.is_authenticated:
        num_products = Product.objects.all().count()
        products = Product.objects.all()
        context = {
            'num_products': num_products,
            'products': products,
        }
        return render(request, 'dashboard.html',context=context)
    else:
        return redirect('home')

def Products(request):
    if request.user.is_authenticated:
        num_products = Product.objects.all().count()
        products = Product.objects.all().order_by('stock')
        context = {
            'num_products': num_products,
            'products': products,
        }
        return render(request, 'products.html',context=context)
    else:
        return redirect('home')
    
def Brands(request):
    if request.user.is_authenticated:
        num_brands = Brand.objects.all().count()
        brands = Brand.objects.all().order_by('name')
        context = {
            'num_brands': num_brands,
            'brands': brands,
        }
        return render(request, 'brands.html',context=context)
    else:
        return redirect('home')
    
def Categories(request):
    if request.user.is_authenticated:
        num_categories = Category.objects.all().count()
        categories = Category.objects.all().order_by('name')
        context = {
            'num_categories': num_categories,
            'categories': categories,
        }
        return render(request, 'categories.html',context=context)
    else:
        return redirect('home')
