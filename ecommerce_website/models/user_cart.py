from django.db import models
from django.contrib.auth.models import User
from ecommerce_website.models.product import Product
from ecommerce_website.models.size import Size
from ecommerce_website.models.color import Color

class UserCart(models.Model):
    user_id  = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id  = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)