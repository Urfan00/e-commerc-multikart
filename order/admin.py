from django.contrib import admin
from .models import Basket, BasketItem, Wishlist


admin.site.register([Basket, BasketItem, Wishlist])
