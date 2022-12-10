from django.urls import path
from products.api.views import BrandAPI, BrandReadUpdateDeleteView, CategoryAPI, CategoryReadUpdateDeleteView, ColorAPI, ColorReadUpdateDeleteView, ProductAPI, ProductReadUpdateDeleteView, ProductVersionAPI, ProductVersionReadUpdateDeleteView, SizeAPI, SizeReadUpdateDeleteView



urlpatterns = [
    path('products/', ProductAPI.as_view(), name = 'api_products'),
    path('products/<int:pk>/', ProductReadUpdateDeleteView.as_view(), name = 'api_products'),

    path('product_version/', ProductVersionAPI.as_view(), name = 'api_product_version'),
    path('product_version/<int:pk>/', ProductVersionReadUpdateDeleteView.as_view(), name = 'api_product_version'),

    path('categories/', CategoryAPI.as_view(), name = 'api_categories'),
    path('categories/<int:pk>/', CategoryReadUpdateDeleteView.as_view(), name = 'api_categories'),

    path('brands/', BrandAPI.as_view(), name = 'api_brands'),
    path('brands/<int:pk>/', BrandReadUpdateDeleteView.as_view(), name = 'api_brands'),

    path('sizes/', SizeAPI.as_view(), name = 'api_sizes'),
    path('sizes/<int:pk>/', SizeReadUpdateDeleteView.as_view(), name = 'api_sizes'),

    path('colors/', ColorAPI.as_view(), name = 'api_colors'),
    path('colors/<int:pk>/', ColorReadUpdateDeleteView.as_view(), name = 'api_colors'),
]
