from django.shortcuts import render
from ecommerce_website.models.category import Category
from ecommerce_website.models.product import Product
from ecommerce_website.helpers.helper import *

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all().prefetch_related('productimage_set')
  
    context = getDefault(request)
    
    return render(request,'web/home.html',
                  {
                    **context,
                   'categories': categories,
                   'products': products,
                   })

def about(request):
    context = getDefault(request)
    return render(request, 'web/about_us.html',{**context})

def contact(request):
    context = getDefault(request)
    return render(request, 'web/contact.html', {**context})

