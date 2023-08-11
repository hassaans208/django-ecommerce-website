from django.db import models
from django.contrib.auth.models import User
from ecommerce_website.models.address import Address

class PaymentMethod(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    billing_address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    card_number = models.CharField(max_length=18, null=True)
    expiry_date = models.DateField(max_length=18, null=True)
    cvc = models.IntegerField(null=True)
    account_title = models.CharField(max_length=20)
    address  = models.CharField(max_length=90, null=True)
    country  = models.CharField(max_length=90, null=True)
    state  = models.CharField(max_length=90, null=True)
    city  = models.CharField(max_length=90, null=True)
    phone_number  = models.CharField(max_length=14, null=True)
