from django.db import models

class FooterMenu(models.Model):
    name  = models.CharField(max_length=90, unique=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)