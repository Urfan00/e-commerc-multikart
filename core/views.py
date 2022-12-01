from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def profile(request):
    return render(request, 'profile.html')


def about(request):
    return render(request, 'about-page.html')


def error(request):
    return render(request, '404.html')


def faq(request):
    return render(request, 'faq.html')
