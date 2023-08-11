from django.urls import path
from ecommerce_website.views.web.authView import *

urlpatterns = [
    path('login', login, name='login' ),
    path('register', register, name='register' ),
    path('change-password', change_password, name='change_password' ),
    path('logout', logout, name='logout' ),
]
