# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.shortcuts import render,redirect
from .models import Product

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

