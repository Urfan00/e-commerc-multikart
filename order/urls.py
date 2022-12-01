from django.urls import path
from .views import basket, checkout, ordersuccess, wishlist

urlpatterns = [
    path('basket/', basket, name = 'basket'),
    path('checkout/', checkout, name = 'checkout'),
    path('ordersuccess/', ordersuccess, name = 'ordersuccess'),
    path('wishlist/', wishlist, name = 'wishlist'),
]
