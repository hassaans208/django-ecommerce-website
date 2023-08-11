from django.urls import path
from ecommerce_website.views.web.userView import *

urlpatterns = [
    path('wishlist', wishlist, name='wishlist'),
    path('add-wishlist/<int:pk>', add_to_wishlist, name='add_to_wishlist'),
    path('remove-wish/<int:pk>', remove_wish, name='remove_wish'),
    path('profile', profile, name='profile'),
    path('cart', cart, name='cart'),
    path('add-cart/<int:pk>', add_to_cart, name='add_to_cart'),
    path('rm-cart/<int:pk>', remove_cart_item, name='remove_cart_item'),
]
