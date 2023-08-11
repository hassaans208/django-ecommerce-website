from ecommerce_website.models.app_setting import AppSetting
from ecommerce_website.models.user_cart import UserCart
from ecommerce_website.models.user_wishlist import UserWishlist
from ecommerce_website.models.user_profile import UserProfile
from django.db.models import Count
from django.contrib.auth.models import User


def getAccount(request):
    user = None
    if request.user.is_authenticated:
        try:
            user = UserProfile.objects.select_related('user').get(user=request.user)
        except UserProfile.DoesNotExist:
            user = UserProfile.objects.create(user=request.user)
        print(user)
    return user

def getDefault(request):
    app_setting = AppSetting.objects.first()
    logged_in = False
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = UserCart.objects.filter(user_id=request.user).annotate(cart_count = Count('product_id'))
        cart_count = cart_count.count()
    else:
        cart_count = 0
    if request.user.is_authenticated:
        wishlist_count = UserWishlist.objects.filter(user_id=request.user).annotate(wishlist_count = Count('product_id'))
        wishlist_count = wishlist_count.count()
    else:
        wishlist_count = 0     
    logged_in = request.user.is_authenticated
    
    return {
        'app_setting': app_setting,
        'cart_count': cart_count,
        'wishlist_count': wishlist_count,
        'logged_in': logged_in,
        }
