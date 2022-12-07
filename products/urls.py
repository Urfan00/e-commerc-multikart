from django.urls import path
from .views import ProductListView, ProductDetailView, SearchResultsView, vendorprofile



urlpatterns = [
    path('products_list/', ProductListView.as_view(), name = 'products_list'),
    path('product_detail/<slug:slug>', ProductDetailView.as_view(), name = 'product_detail'),
    path('search/', SearchResultsView.as_view(), name = 'search'),
    path('vendor_profile/', vendorprofile, name = 'vendor_profile'),
]
