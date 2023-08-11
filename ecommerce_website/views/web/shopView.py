from django.shortcuts import render
from ecommerce_website.models.product import Product
from ecommerce_website.models.category import Category
from ecommerce_website.models.brand import Brand
from ecommerce_website.models.size import Size
from ecommerce_website.models.color import Color
from ecommerce_website.helpers.helper import *


def shop(request):
    context = getDefault(request)

    products = Product.objects.all().prefetch_related('productimage_set')
    categories  = Category.objects.all().annotate(product_count = Count('product'))
    brands  = Brand.objects.all().annotate(product_count = Count('product'))
    sizes  = Size.objects.all()
    colors  = Color.objects.all()
    return render(request, 'shop/shop.html',
    {
    'products': products,
    'categories': categories,
    'brands': brands,
    'sizes': sizes,
    'colors': colors,
    **context
    })

def product(request, pk):
    products = Product.objects.select_related('brand', 'category').prefetch_related('productimage_set', 'producthascolor_set__color', 'producthassize_set__size').get(id=pk)
    # for product_has_color in products.producthascolor_set.all():
    #     size_name = product_has_color.color.hex
    #     print(size_name)
    product_all = Product.objects.all().prefetch_related('productimage_set')
    context = getDefault(request)
    return render(request, 'shop/product.html', {'product': products, **context, 'products': product_all})
