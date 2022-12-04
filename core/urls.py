from django.urls import path
from .views import AboutListView, CreateContactView, Faq, IndexView, error


urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('contact/', CreateContactView.as_view(), name = 'contact'),
    path('about_us/', AboutListView.as_view(), name = 'about_us'),
    path('faq/', Faq.as_view(), name = 'faq'),
    path('error/', error, name = 'error'),
]
