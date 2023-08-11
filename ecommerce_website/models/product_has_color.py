from django.db import models
from ecommerce_website.models.product import Product
from ecommerce_website.models.color import Color

class ProductHasColor(models.Model):
    color  = models.ForeignKey(Color, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)