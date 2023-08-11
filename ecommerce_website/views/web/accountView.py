from django.shortcuts import render, redirect
from ecommerce_website.helpers.helper import *
from django.contrib.auth.decorators import login_required
from ecommerce_website.models.address import Address
from django.db.models import Q
from django.contrib import messages

@login_required(login_url="/auth/login")
def account(request):
    context = getDefault(request)
    return render(request, 'user/account.html', {**context})

@login_required(login_url="/auth/login")
def address(request):
    context = getDefault(request)
    u_profile = getAccount(request)
    billing = Address.objects.get((Q(user=request.user) & Q(address_type='B')))
    shipping = Address.objects.get((Q(user=request.user) & Q(address_type='S')))
    return render(request, 'user/address.html', {**context, 'profile':u_profile, 'billing':billing, 'shipping':shipping})

@login_required(login_url="/auth/login")
def update_address(request, type):
    if request.method == 'POST':
        char  = "S" if type == 'shipping' else 'B' 
        address = Address.objects.get((Q(user=request.user) & Q(address_type=char)))
        address.full_name = request.POST.get('full_name')
        address.address = request.POST.get('address')
        address.country = request.POST.get('country')
        address.state = request.POST.get('state')
        address.city = request.POST.get('city')
        address.postal_code = request.POST.get('postal_code')
        address.phone_number = request.POST.get('phone_number')
        address.save()
        messages.success(request, 'Address updated successfully')
        return redirect('address')
    else:
        title = 'Shipping' if type == 'shipping' else 'Billing'
        char  = "S" if type == 'shipping' else 'B' 
        try:
            address = Address.objects.get((Q(user=request.user) & Q(address_type=char)))
        except Address.DoesNotExist:
            address = Address.objects.create(address_type=char, user=request.user)
        context = getDefault(request)
        u_profile = getAccount(request)
        return render(request, 'user/update_address.html', {**context,'address': address, 'profile':u_profile, 'title': title, 'type': type})

@login_required(login_url="/auth/login")
def payment_methods(request):
    context = getDefault(request)
    u_profile = getAccount(request)
    billing = Address.objects.get((Q(user=request.user) & Q(address_type='B')))
    shipping = Address.objects.get((Q(user=request.user) & Q(address_type='S')))
    return render(request, 'user/payment_method.html', {**context, 'profile':u_profile, 'billing':billing, 'shipping':shipping})
