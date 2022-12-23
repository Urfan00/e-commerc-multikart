from django.urls import path
from .views import BasketView, CheckoutView, OrderView, WishlistView

urlpatterns = [
    path('wishlist/', WishlistView.as_view(), name = 'wishlist'),
    path('basket/', BasketView.as_view(), name = 'basket'),
    path('checkout/', CheckoutView.as_view(), name = 'checkout'),
    path('order_success/', OrderView.as_view(), name = 'order_success'),
]
