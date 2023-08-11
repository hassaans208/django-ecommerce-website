from django.db import models
from django.contrib.auth.models import User
from ecommerce_website.models.product import Product

class ProductHasReview(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating  = models.IntegerField()
    review = models.CharField(max_length=120)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)