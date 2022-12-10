from rest_framework import serializers
from products.models import Brand, Category, Color, ProductVersion, Products, Size



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class BrandReadSerializer(serializers.ModelSerializer):
    category_id = CategorySerializer()

    class Meta:
        model = Brand
        fields = ['id', 'name', 'category_id']


class BrandCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ['id', 'name', 'category_id']


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name']


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name']


class ProductReadSerializer(serializers.ModelSerializer):
    brand_id = BrandReadSerializer()
    category_id = CategorySerializer()
    detail_url = serializers.SerializerMethodField()

    def get_detail_url(self, obj):
        return obj.get_absolute_url()

    class Meta:
        model = Products
        fields = fields = [
            'id',
            'product_name',
            'product_details',
            'short_description',
            'long_description',
            'price',
            'new_price',
            'discount',
            'slug',
            'cover_image',
            'brand_id',
            'category_id',
            'detail_url',
            'created_at',
            'update_at'
        ]


class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = fields = [
            'id',
            'product_name',
            'product_details',
            'short_description',
            'long_description',
            'price',
            'new_price',
            'discount',
            'cover_image',
            'brand_id',
            'category_id',
            'created_at',
            'update_at'
        ]


class ProductVersionReadSerializer(serializers.ModelSerializer):

    size_id = SizeSerializer(many=True)
    color_id = ColorSerializer(many=True)
    product_id = ProductReadSerializer()


    class Meta:
        model = ProductVersion
        fields = fields = [
            'id',
            'quantity',
            'rate_avg',
            'review_count',
            'read_count',
            'size_id',
            'color_id',
            'product_id',
            'images_id',
            'created_at',
            'update_at'
        ]


class ProductVersionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductVersion
        fields = fields = [
            'id',
            'quantity',
            'size_id',
            'color_id',
            'product_id',
            'images_id',
        ]
