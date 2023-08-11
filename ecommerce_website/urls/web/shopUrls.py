from django.urls import path
from ecommerce_website.views.web.shopView import *

urlpatterns = [
    path('product/<int:pk>', product, name='product'),
    path('shop', shop, name='shop'),
    # path('checkout', checkout, name='account'),
]
