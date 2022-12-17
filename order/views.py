from django.shortcuts import render
from .models import Wishlist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView



class WishlistView(LoginRequiredMixin, ListView):
    model = Wishlist
    template_name = 'wishlist.html'
    context_object_name = 'wishlists'

    def get_queryset(self):
        user_wishlist =  Wishlist.objects.filter(user_id = self.request.user).first()
        if user_wishlist:
            self.queryset = user_wishlist.product_version_id.all()
        return self.queryset


def basket(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def ordersuccess(request):
    return render(request, 'order-success.html')
