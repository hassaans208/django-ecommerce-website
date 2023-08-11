from django.shortcuts import render, redirect
from ecommerce_website.models.user_wishlist import UserWishlist
from ecommerce_website.models.user_cart import UserCart
from ecommerce_website.models.product import Product
from django.db.models import Q
from django.contrib import messages
from ecommerce_website.helpers.helper import *
from django.contrib.auth.decorators import login_required

@login_required(login_url="/auth/login")
def profile(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        user = User.objects.get(id=request.user.id)
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        user = UserProfile.objects.get(user=user)
        user.dob = dob
        user.gender = gender
        user.phone_number = phone_number
        previous_image = user.image
        if previous_image and image:
            previous_image.delete()
        user.image = image
        user.save()
        messages.success(request, 'User Profile Updated Successfully')
        return redirect('profile')
    else:
        context = getDefault(request)
        u_profile = getAccount(request)    
        return render(request, 'user/profile.html',{**context, 'profile':u_profile})
        
@login_required(login_url="/auth/login")
def account(request):
    context = getDefault(request)
    u_profile = getAccount(request)
    return render(request, 'user/account.html',{**context, 'profile':u_profile, 'user': request.user})

@login_required(login_url="/auth/login")
def wishlist(request):
    context = getDefault(request)
    u_profile = getAccount(request)    
    wishlist = UserWishlist.objects.filter(user_id=request.user).select_related('product_id').prefetch_related('product_id__productimage_set')
    return render(request, 'user/wishlist.html', {'wishlist': wishlist, **context, 'profile':u_profile})


def add_to_wishlist(request, pk):
    product = Product.objects.filter(id=pk)
    wishlist = UserWishlist.objects.filter(Q(user_id=request.user) & Q(product_id=product[0])).exists()
    if wishlist:
        return redirect('/')
    else:
        UserWishlist.objects.create(user_id=request.user, product_id=product[0])
        return redirect('/')

def remove_wish(request, pk):
    UserWishlist.objects.filter(id=pk).delete()
    return redirect('/')
    

    
@login_required(login_url="/auth/login")
def cart(request):
    context = getDefault(request)
    u_profile = getAccount(request)    
    cart = UserCart.objects.filter(user_id=request.user).select_related('product_id').prefetch_related('product_id__productimage_set','product_id__producthascolor_set__color', 'product_id__producthassize_set__size')
    return render(request, 'user/cart.html', {'cart': cart, **context, 'profile':u_profile})

def add_to_cart(request, pk):
    product = Product.objects.filter(id=pk)
    cart = UserCart.objects.filter(Q(user_id=request.user) & Q(product_id=product[0])).exists()
    if cart:
        messages.error(request,'Product already in cart')
        return redirect('/')
    else:
        messages.success(request,'Product added to cart')
        UserCart.objects.create(user_id=request.user, product_id=product[0])
        return redirect('/')
    

def remove_cart_item(request, pk):
    UserCart.objects.filter(id=pk).delete()
    return redirect('/')