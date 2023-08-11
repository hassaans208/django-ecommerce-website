from django.db import models
from ecommerce_website.models.brand import Brand
from ecommerce_website.models.category import Category
from ecommerce_website.models.product_status import ProductStatus
from ecommerce_website.models.color import Color
from ecommerce_website.models.size import Size

    
    
class Product(models.Model):
    
    PRODUCT_TYPE = [
            ('NP', 'Brand new product'),
            ('UP', 'Used product')
    ]
    
    PRODUCT_STATUS = [
            ('A', 'Available'),
            ('O', 'Out of stock'),
    ]
    
    title  = models.CharField(max_length=220)
    description = models.TextField(max_length=600)
    sku  = models.CharField(max_length=90, unique=True)
    brand = models.ForeignKey(Brand,null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, default='A', choices=PRODUCT_STATUS)
    material  = models.CharField(max_length=20)
    product_type  = models.CharField(max_length=2, choices=PRODUCT_TYPE)
    available_quantity = models.IntegerField()
    total_quantity = models.IntegerField()
    weight = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    taxes = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)