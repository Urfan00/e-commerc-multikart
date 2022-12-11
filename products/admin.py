from django.contrib import admin
from .models import Brand, Category, Color, Image, Products, ProductVersion, ProductReview, Size
from modeltranslation.admin import TranslationAdmin



class BrandAdmin(TranslationAdmin):
    pass


class CategoryAdmin(TranslationAdmin):
    pass


class ColorAdmin(TranslationAdmin):
    pass


class ProductAdmin(TranslationAdmin):
    pass


class SizeAdmin(TranslationAdmin):
    pass


admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Image)
admin.site.register(Products, ProductAdmin)
admin.site.register(ProductVersion)
admin.site.register(ProductReview)
admin.site.register(Size, SizeAdmin)
