from django.urls import path
from ecommerce_website.views.web.apiView import *

urlpatterns = [
    path('add-wishlist/<int:pk>', add_to_wishlist, name='api_add_to_wishlist'),
    path('rm-wish/<int:pk>', remove_wish, name='api_remove_wish'),
    path('add-cart/<int:pk>', add_to_cart, name='api_add_to_cart'),
    path('add-cart-common/<int:pk>', add_to_cart_common, name='add_to_cart_common'),
    path('rm-cart/<int:pk>', remove_cart_item, name='api_remove_cart_item'),
    path('get-product/<int:pk>', get_product, name='api_get_product'),
]
