from django.urls import path
from .views import BasketView, WishlistView, checkout, ordersuccess

urlpatterns = [
    path('wishlist/', WishlistView.as_view(), name = 'wishlist'),
    path('basket/', BasketView.as_view(), name = 'basket'),

    path('checkout/', checkout, name = 'checkout'),
    path('order_success/', ordersuccess, name = 'order_success'),
]
