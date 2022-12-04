from django.urls import path
from .views import productslist, productdetail, search, vendorprofile

urlpatterns = [
    path('products_list/', productslist, name = 'products_list'),
    path('product_detail/', productdetail, name = 'product_detail'),
    path('search/', search, name = 'search'),
    path('vendor_profile/', vendorprofile, name = 'vendor_profile'),
]
