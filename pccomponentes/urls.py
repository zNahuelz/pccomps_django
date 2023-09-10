"""
URL configuration for pccomponentes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from account.views import Dashboard,Products,Brands,Categories,NewProduct,NewBrand,NewCategory,EditProduct,ProductDetail,DeleteProduct,EditCategory,EditBrand,UserProfile,ChangePassword
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("account.urls")),
    path('',TemplateView.as_view(template_name='home.html'),name='home'),
    path('dashboard/',view=Dashboard,name='dashboard'),
    path('products/',view=Products,name='products'),
    path('brands/',view=Brands,name='brands'),
    path('categories/',view=Categories,name='categories'),
    path('new-product/',view=NewProduct,name='new_product'),
    path('brands/new/',view=NewBrand,name='new_brand'),
    path('categories/new/',view=NewCategory,name='new_category'),
    path('products/edit/<id>/',view=EditProduct,name='edit_product'),
    path('products/detail/<id>/',view=ProductDetail,name='product_detail'),
    path('products/delete/<id>/',view=DeleteProduct,name='delete_product'),
    path('categories/edit/<id>/',view=EditCategory,name='edit_category'),
    path('brands/edit/<id>/',view=EditBrand,name='edit_brand'),
    path('user/profile/',view=UserProfile,name='user_profile'),
    path('user/change_password/',view=ChangePassword,name='change_password'),
]
