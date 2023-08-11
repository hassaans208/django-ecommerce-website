from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    
    ADDRESS_TYPE = [
        ('B', 'Billing Address'),
        ('S', 'Shipping Address'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=90, null=True)
    address_type  = models.CharField(choices=ADDRESS_TYPE,max_length=1, default="S")
    address  = models.CharField(max_length=90, null=True)
    country  = models.CharField(max_length=90, null=True)
    state  = models.CharField(max_length=90, null=True)
    city  = models.CharField(max_length=90, null=True)
    phone_number  = models.CharField(max_length=14, null=True)
    postal_code  = models.CharField(max_length=9, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)