from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    
    GENDER = [
        ('M', "Male"),
        ('F', "Female"),
        ('O', "Other")
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=14, null=True)
    gender = models.CharField(max_length=1, choices=GENDER, default="M", null=True)
    image = models.ImageField(upload_to="static/user_profile_pictures", height_field=None, width_field=None, max_length=None, null=True)
    dob = models.DateField(auto_now=False, auto_now_add=False, null=True)
    created_at  = models.DateTimeField(auto_now_add=True, null=True)
    updated_at  = models.DateTimeField(auto_now_add=True, null=True)