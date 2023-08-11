from django.db import models
from django.contrib.auth.models import User
from ecommerce_website.models.product import Product

class UserWishlist(models.Model):
    user_id  = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id  = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)