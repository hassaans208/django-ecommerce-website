from django.db import models
from django.contrib.auth.models import User
from ecommerce_website.models.product import Product
from ecommerce_website.models.color import Color
from ecommerce_website.models.size import Size

class Order(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    color  = models.ForeignKey(Color, on_delete=models.CASCADE)
    size  = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_id  = models.UUIDField(unique=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)