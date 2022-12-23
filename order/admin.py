from django.contrib import admin
from .models import Basket, BasketItem, BillingAddress, Order, Wishlist


admin.site.register([Basket, BasketItem, BillingAddress, Order, Wishlist])
