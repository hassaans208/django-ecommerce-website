from django.shortcuts import render
from django.db.models import Sum
from ecommerce_website.models.user_cart import UserCart
from ecommerce_website.helpers.helper import *
from django.contrib.auth.decorators import login_required

@login_required(login_url="/auth/login")
def checkout(request):
    
    context = getDefault(request)
    cart = UserCart.objects.filter(user_id=request.user).select_related('product_id').prefetch_related('product_id__productimage_set')
    cost = UserCart.objects.filter(user_id=request.user).select_related('product_id').prefetch_related('product_id__productimage_set').aggregate(cost=Sum('product_id__price'))
    return render(request, 'shop/checkout.html', {'cart': cart, 'subtotal': cost['cost'] if cost['cost'] else 0 , **context})

@login_required(login_url="/auth/login")
def order(request):
    context = getDefault(request)
    return render(request, 'order/orders.html', {**context})
