from django.shortcuts import render
from .models import *


# Create your views here.

def all_products(request):
    products  = Product.objects.all()
    categories = Category.objects.all()
    context = {'products':products,'categories':categories}
    return render(request,'product/allproducts.html',context)