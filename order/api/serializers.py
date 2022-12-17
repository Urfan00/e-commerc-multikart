from rest_framework import serializers
from order.models import Wishlist
from products.api.serializers import ProductVersionReadSerializer



class WishlistSerializer(serializers.ModelSerializer):
    product_version_id = ProductVersionReadSerializer(many=True)

    class Meta:
        model = Wishlist
        fields = ['id', 'user_id', 'product_version_id']
