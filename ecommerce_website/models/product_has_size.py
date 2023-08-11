from django.db import models
from ecommerce_website.models.product import Product
from ecommerce_website.models.size import Size

class ProductHasSize(models.Model):
    size  = models.ForeignKey(Size, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)