from django.db import models

class AppSetting(models.Model):
    logo = models.ImageField(upload_to='static/app_settings/logo', height_field=None, width_field=None, max_length=None)
    main_image = models.ImageField(upload_to='static/app_settings/main_image', height_field=None, width_field=None, max_length=None)
    ad_banner = models.ImageField(upload_to='static/app_settings/banner', height_field=None, width_field=None, max_length=None)
    website_title = models.TextField(max_length=220)
    website_desc = models.TextField(max_length=220)
    footer_text = models.TextField(max_length=220)
    about_us_title = models.TextField(max_length=220)
    about_us_desc = models.TextField(max_length=220)
    contact_us_title = models.TextField(max_length=220)
    contact_us_desc = models.TextField(max_length=220)
    copyright_text = models.TextField(max_length=220)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)