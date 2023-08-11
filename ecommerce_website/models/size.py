from django.db import models

class Size(models.Model):
    display_name  = models.CharField(max_length=90, unique=True)
    name  = models.CharField(max_length=90, unique=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)