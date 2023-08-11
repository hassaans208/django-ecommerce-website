from django.urls import path
from ecommerce_website.views.web.orderView import *

urlpatterns = [
    path('checkout', checkout,  name='checkout'),
    path('order', order,  name='order'),
]
