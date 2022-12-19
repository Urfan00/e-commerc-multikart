from rest_framework import serializers
from order.models import Basket, BasketItem, Wishlist
from products.api.serializers import ProductVersionReadSerializer



class WishlistSerializer(serializers.ModelSerializer):
    product_version_id = ProductVersionReadSerializer(many=True)

    class Meta:
        model = Wishlist
        fields = ['id', 'user_id', 'product_version_id']


class BasketItemSerializer(serializers.ModelSerializer):
    product_version_id = ProductVersionReadSerializer()

    class Meta:
        model = BasketItem
        fields = ['id', 'quantity', 'product_version_id', 'basket_id']


class BasketSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source='user_id.username')
    basket_items = BasketItemSerializer(many=True)

    class Meta:
        model = Basket
        fields = ['id', 'user_id', 'is_active', 'created_at', 'update_at', 'basket_items']
