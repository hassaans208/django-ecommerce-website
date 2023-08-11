from django.shortcuts import render, redirect
from ecommerce_website.models.user_wishlist import UserWishlist
from ecommerce_website.models.user_cart import UserCart
from ecommerce_website.models.product import Product
from ecommerce_website.models.size import Size
from ecommerce_website.models.color import Color
from django.db.models import Q
from ecommerce_website.helpers.helper import *
from django.http import JsonResponse
from django.core import serializers
def add_to_wishlist(request, pk):
    product = Product.objects.filter(id=pk)
    wishlist = UserWishlist.objects.filter(Q(user_id=request.user) & Q(product_id=product[0])).exists()
    if wishlist:
        data = {'status': False, 'message': 'Item already exists in wishlist'}
        return JsonResponse(data)
    else:
        UserWishlist.objects.create(user_id=request.user, product_id=product[0])
        data = {'status': True, 'message': 'Item Added in wishlist'}
        return JsonResponse(data)

def remove_wish(request, pk):
    UserWishlist.objects.filter(id=pk).delete()
    data = {'status': True, 'message': 'Item removed from wishlist'}
    return JsonResponse(data)
    
def add_to_cart(request, pk):
    product = Product.objects.filter(id=pk)
    cart = UserCart.objects.filter(Q(user_id=request.user) & Q(product_id=product[0])).exists()
    if cart:
        data = {'status': False, 'message': 'Item already exists in cart, Go to Cart to modify Item!'}
        return JsonResponse(data)
    else:
        size = Size.objects.get(id=request.GET.get('size'))
        color = Color.objects.get(id=request.GET.get('color'))
        UserCart.objects.create(user_id=request.user, product_id=product[0], size=size, quantity=request.GET.get('qty'), color=color)
        data = {'status': True, 'message': 'Item added in cart'}
        return JsonResponse(data)    

def add_to_cart_common(request, pk):
    product = Product.objects.filter(id=pk)
    cart = UserCart.objects.filter(Q(user_id=request.user) & Q(product_id=product[0])).exists()
    if cart:
        data = {'status': False, 'message': 'Item already exists in cart, Go to Cart to modify Item!'}
        return JsonResponse(data)
    else:
        UserCart.objects.create(user_id=request.user, product_id=product[0])
        data = {'status': True, 'message': 'Item added in cart'}
        return JsonResponse(data)    

def remove_cart_item(request, pk):
    UserCart.objects.filter(id=pk).delete()
    data = {'status': True, 'message': 'Item removed from cart'}
    return JsonResponse(data)  

def get_product(request, pk):
    data = Product.objects.prefetch_related('productimage_set', 'producthascolor_set__color', 'producthassize_set__size').get(id=pk)
    # serialized_products = serializers.serialize('json', data)
    data = {
        'status': True, 
        'message': 'Item fetched Successfully', 
        'data':  {
            'name': data.title,
            'price': data.price,
            'total_price': data.total_price,
            'discounted_price': data.discounted_price,
            'available_quantity': data.available_quantity,
            'images': [image.images.url for image in data.productimage_set.all()],
            'colors': [color.color.hex for color in data.producthascolor_set.all()],
            'sizes': [size.size.display_name for size in data.producthassize_set.all()],},
            'colors_ids': [color.color.id for color in data.producthascolor_set.all()],
            'sizes_ids': [size.size.id for size in data.producthassize_set.all()],
        }
    return JsonResponse(data)
    