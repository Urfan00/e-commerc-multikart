from django.shortcuts import render


def basket(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def ordersuccess(request):
    return render(request, 'order-success.html')


def wishlist(request):
    return render(request, 'wishlist.html')
