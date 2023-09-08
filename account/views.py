# accounts/views.py
from django.urls import reverse_lazy
from django.db.models import Sum
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm,ProductForm,BrandForm,CategoryForm
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
        amount = Product.objects.aggregate(Sum('stock'))
        products_price = Product.objects.aggregate(Sum('sell_price'))
        context = {
            'num_products': num_products,
            'products': products,
            'amount': amount['stock__sum'],
            'products_price': round(products_price['sell_price__sum'],2),
        }
        return render(request, 'products/products.html',context=context)
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
        return render(request, 'brands/brands.html',context=context)
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
        return render(request, 'categories/categories.html',context=context)
    else:
        return redirect('home')

def NewProduct(request):
    if request.user.is_authenticated:
        context = {
            'form': ProductForm()
        }
        if request.method == 'POST':
            form = ProductForm(data=request.POST)
            if form.is_valid():
                form.save()
                context['alert'] = 1
            else:
                context['alert'] = 0

        return render(request, 'products/new_product.html',context=context)
    else:
        return redirect('home')
    
def NewBrand(request):
    if request.user.is_authenticated:
        context = {
            'form': BrandForm()
        }
        if request.method == 'POST':
            form = BrandForm(data=request.POST)
            if form.is_valid():
                form.save()
                context['alert'] = 1
            else:
                context['alert'] = 0   

        return render(request,'brands/new_brand.html',context=context)
    else:
        return redirect('home')
    
def NewCategory(request):
    if request.user.is_authenticated:
        context = {
            'form': CategoryForm()
        }
        if request.method == 'POST':
            form = CategoryForm(data=request.POST)
            if form.is_valid():
                form.save()
                context['alert'] = 1
            else:
                context['alert'] = 0   

        return render(request,'categories/new_category.html',context=context)
    else:
        return redirect('home')