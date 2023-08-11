from django.db import models
from django.contrib.auth.models import User
from .tax_or_exemtion import TaxOrExemption
from .product import Product

class ProductHasTax(models.Model):
    tax_id  = models.ForeignKey(TaxOrExemption, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    value_in_percent  = models.IntegerField()
    actual_value  = models.DecimalField(max_digits=10, decimal_places=2)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)