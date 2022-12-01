from django.urls import path
from .views import productslist, productdetail, search, vendorprofile

urlpatterns = [
    path('productslist/', productslist, name = 'productslist'),
    path('productdetail/', productdetail, name = 'productdetail'),
    path('search/', search, name = 'search'),
    path('vendorprofile/', vendorprofile, name = 'vendorprofile'),
]
