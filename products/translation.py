from modeltranslation.translator import translator, TranslationOptions
from .models import Brand, Category, Color, Products, Size



class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


class BrandTranslationOptions(TranslationOptions):
    fields = ('name',)


class SizeTranslationOptions(TranslationOptions):
    fields = ('name',)


class ColorTranslationOptions(TranslationOptions):
    fields = ('name',)


class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name', 'product_details', 'short_description', 'long_description', 'slug',)


translator.register(Category, CategoryTranslationOptions)
translator.register(Brand, BrandTranslationOptions)
translator.register(Size, SizeTranslationOptions)
translator.register(Color, ColorTranslationOptions)
translator.register(Products, ProductTranslationOptions)
