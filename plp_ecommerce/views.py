# from django.shortcuts import render
# # from django.http import HttpResponse
# from .models import Product
# # Create your views here.

# def product_list(request):
#     products = Product.objects.all()
#     context = {
#         'products': products
#     }
#     return render(request,'plp_ecommerce/product_list.html',context)

from django.shortcuts import render
from .models import product

# Create your views here.
def product_list(request):
    products = product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'plp_ecommerce/product_list.html', context)