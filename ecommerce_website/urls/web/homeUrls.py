from django.urls import path
from ecommerce_website.views.web.homeView import *

urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
]
