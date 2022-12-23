import datetime
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import Q
from .forms import BillingAddressFromModel
from .models import Basket, BasketItem, Order, Wishlist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView



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


class CheckoutView(LoginRequiredMixin , CreateView):
    template_name = 'checkout.html'
    form_class = BillingAddressFromModel
    success_url = reverse_lazy('order_success')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        basket = Basket.objects.filter(user_id=self.request.user, is_active=True).first()
        products = BasketItem.objects.filter(basket_id__user_id = self.request.user, basket_id__is_active = True).all()

        total_price = 0

        if form.is_valid():
            billing_address_form = form.save(commit=False)
            billing_address_form.user_id = self.request.user
            billing_address_form.save()


            for product in products:
                total_price += product.get_subtotal()
                product.product_version_id.quantity -= product.quantity
                product.product_version_id.save()

            order = Order(user_id=self.request.user, address_id=billing_address_form, basket_id=basket)
            order.total += total_price
            order.save()

            basket.is_active = False
            basket.save()

        return redirect('order_success')


class OrderView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order-success.html'

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        user_order = Order.objects.filter(user_id=self.request.user).last()
        if user_order:
            context['order'] = user_order.basket_id.basket_items.all()
            context['user_order'] = user_order

            total_price = 0
            Tax_GST = 10
            shipping = 12

            for product in context['order']:
                total_price += product.get_subtotal()

            context['tax_gst'] = Tax_GST
            context['shipping'] = shipping
            context['total_price'] = total_price
            context['total'] = Tax_GST +shipping + total_price

            month = datetime.timedelta(days=30)
            expected_date = (user_order.created_at + month).strftime('%B %d, %Y')
            context['expected_date'] = expected_date

        return context
