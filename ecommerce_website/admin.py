from django.contrib import admin

from ecommerce_website.models.app_setting import AppSetting
from ecommerce_website.models.brand import Brand
from ecommerce_website.models.category import Category
from ecommerce_website.models.color import Color
from ecommerce_website.models.footer_has_option import FooterSubMenu
from ecommerce_website.models.footer import FooterMenu
from ecommerce_website.models.material import Material
from ecommerce_website.models.order_status import OrderStatus
from ecommerce_website.models.order import Order
from ecommerce_website.models.product_has_color import ProductHasColor
from ecommerce_website.models.product_has_size import ProductHasSize
from ecommerce_website.models.product_has_image import ProductImage
from ecommerce_website.models.product_has_review import ProductHasReview
from ecommerce_website.models.product_has_tax import ProductHasTax
from ecommerce_website.models.product_status import ProductStatus
from ecommerce_website.models.product import Product
from ecommerce_website.models.size import Size
from ecommerce_website.models.tax_or_exemtion import TaxOrExemption
from ecommerce_website.models.user_cart import UserCart
from ecommerce_website.models.user_wishlist import UserWishlist
from ecommerce_website.models.address import Address
from ecommerce_website.models.user_profile import UserProfile

admin.site.register(AppSetting)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(FooterSubMenu)
admin.site.register(FooterMenu)
admin.site.register(Material)
admin.site.register(OrderStatus)
admin.site.register(Order)
admin.site.register(ProductImage)
admin.site.register(ProductHasSize)
admin.site.register(ProductHasColor)
admin.site.register(ProductHasReview)
admin.site.register(ProductHasTax)
admin.site.register(ProductStatus)
admin.site.register(Product)
admin.site.register(Size)
admin.site.register(TaxOrExemption)
admin.site.register(UserCart)
admin.site.register(UserWishlist)
admin.site.register(Address)
admin.site.register(UserProfile)
