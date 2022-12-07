from django.contrib import admin
from .models import Brand, Category, Color, Image, Products, ProductVersion, ProductReview, Size


admin.site.register([Brand, Category, Color, Image, Products, ProductVersion, ProductReview, Size])
