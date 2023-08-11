from django.db import models

class Color(models.Model):
    display_name  = models.CharField(max_length=90, unique=True)
    hex  = models.CharField(max_length=10, unique=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)