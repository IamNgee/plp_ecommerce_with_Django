from django.urls import path
from . import views

urlpatterns = [
    # path('index/', views.index, name='index'),
    path('product_list/', views.product_list, name='product_list')
]