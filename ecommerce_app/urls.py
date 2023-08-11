from django.contrib import admin
from django.urls import path, include
from ecommerce_website.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ecommerce_website.urls.web.homeUrls')),
    path('auth/', include('ecommerce_website.urls.web.authUrls')),
    path('', include('ecommerce_website.urls.web.accountUrls')),
    path('', include('ecommerce_website.urls.web.userUrls')),
    path('', include('ecommerce_website.urls.web.shopUrls')),
    path('', include('ecommerce_website.urls.web.orderUrls')),
    path('api/', include('ecommerce_website.urls.web.apiUrls')),
]
