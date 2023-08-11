from django.db import models
from .footer import FooterMenu

class FooterSubMenu(models.Model):
    name  = models.CharField(max_length=90, unique=True)
    footer_menu  = models.ForeignKey(FooterMenu, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at_at  = models.DateTimeField(auto_now_add=True)