from django.urls import path
from .views import error, faq, index, contact, about, profile

urlpatterns = [
    path('error/', error, name = 'error'),
    path('faq/', faq, name = 'faq'),
    path('', index, name = 'index'),
    path('contact/', contact, name = 'contact'),
    path('about_us/', about, name = 'about-us'),
    path('profile/', profile, name = 'profile'),
]
