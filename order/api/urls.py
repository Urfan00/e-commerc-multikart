from django.urls import path
from .views import WishlistAPI



urlpatterns = [
    path('wishlist/', WishlistAPI.as_view(), name='wishlists')
]
