from django.shortcuts import render


def productslist(request):
    return render(request, 'category-page.html')


def productdetail(request):
    return render(request, 'product-page.html')


def search(request):
    return render(request, 'search.html')


def vendorprofile(request):
    return render(request, 'vendor-profile.html')
