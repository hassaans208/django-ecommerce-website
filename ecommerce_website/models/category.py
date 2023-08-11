from django.db import models

class Category(models.Model):
    main_image = models.ImageField(upload_to='static/categories', height_field=None, width_field=None, max_length=None)
    display_name  = models.CharField(max_length=90, unique=True)
    name  = models.CharField(max_length=90, unique=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)