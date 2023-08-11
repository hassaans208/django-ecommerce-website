from django.urls import path
from ecommerce_website.views.web.accountView import *


urlpatterns = [
    path('account', account, name='account'),
    path('address', address, name='address'),
    path('update-address/<slug:type>', update_address, name='update_address'),
    path('payment-method', payment_methods, name='payment_methods'),
    path('payment-method/<int:pk>', payment_methods, name='payment_methods'),
]
