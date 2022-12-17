from django.urls import path
from .views import WishlistView, basket, checkout, ordersuccess

urlpatterns = [
    path('wishlist/', WishlistView.as_view(), name = 'wishlist'),

    path('basket/', basket, name = 'basket'),
    path('checkout/', checkout, name = 'checkout'),
    path('order_success/', ordersuccess, name = 'order_success'),
]
