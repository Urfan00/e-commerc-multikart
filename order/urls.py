from django.urls import path
from .views import basket, checkout, ordersuccess, wishlist

urlpatterns = [
    path('basket/', basket, name = 'basket'),
    path('checkout/', checkout, name = 'checkout'),
    path('order_success/', ordersuccess, name = 'order_success'),
    path('wishlist/', wishlist, name = 'wishlist'),
]
