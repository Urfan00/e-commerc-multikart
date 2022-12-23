from django.urls import path
from .views import SubscriberEmailView


urlpatterns = [
    path('subscribe/', SubscriberEmailView.as_view(), name='subscribe')
]
