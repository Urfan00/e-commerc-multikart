from django.shortcuts import render
from django.db.models import Q
from .models import Basket, BasketItem, Wishlist
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


class BasketView(LoginRequiredMixin, ListView):
    model = Basket
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super(BasketView, self).get_context_data(**kwargs)
        user_basket =  BasketItem.objects.filter(Q(basket_id__user_id = self.request.user), Q(basket_id__is_active = True)).all()

        if user_basket:
            context['user_basket'] = user_basket

        total_price = 0

        for product in user_basket:
            total_price += product.get_subtotal()
        context['total_price'] = total_price

        return context


def checkout(request):
    return render(request, 'checkout.html')


def ordersuccess(request):
    return render(request, 'order-success.html')
