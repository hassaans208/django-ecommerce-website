from django.db import models
from ecommerce_website.models.product import Product

class ProductImage(models.Model):
    
    IMAGE_STATUS = [
        ("M", "Main"),
        ("S", "Sub")
    ]
    
    product_id =  models.ForeignKey(Product, on_delete=models.CASCADE)
    image_status = models.CharField(choices=IMAGE_STATUS, max_length=2, default="S")
    images  = models.FileField(upload_to='static/product_images', max_length=100)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)