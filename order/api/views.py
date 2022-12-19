from rest_framework.views import APIView
from products.models import ProductVersion
from .serializers import BasketSerializer, WishlistSerializer
from order.models import Basket, BasketItem, Wishlist
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class WishlistAPI(APIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        obj, created = Wishlist.objects.get_or_create(user_id = request.user)
        serializer = self.serializer_class(obj)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product')
        product = ProductVersion.objects.filter(pk=product_id).first()
        if product and self.request.user.is_authenticated:
            wishlist1, created = Wishlist.objects.get_or_create(user_id = request.user)
            wishlist2 = Wishlist.objects.filter(user_id = request.user).first()
            wishlist2.product_version_id.add(product)
            return Response(status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, *args, **kwargs):
        ProductID = request.data.get('product')
        if ProductID:
            user_wishlist = Wishlist.objects.get(user_id = self.request.user)
            product = user_wishlist.product_version_id.get(id = ProductID)
            user_wishlist.product_version_id.remove(product.id)
        return Response(status = status.HTTP_200_OK)


class BasketAPI(APIView):
    serializer_class = BasketSerializer
    http_method_names = ['get', 'post', 'delete']
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        obj, created = Basket.objects.get_or_create(user_id = request.user, is_active = True)
        serializer = self.serializer_class(obj)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        quantity = request.data.get('quantity')
        product_id = request.data.get('product')
        product = ProductVersion.objects.filter(id=product_id).first()

        if product and self.request.user.is_authenticated:
            basket, created = Basket.objects.get_or_create(user_id = request.user, is_active = True)
            basket_item, created = BasketItem.objects.get_or_create(product_version_id = product, basket_id = basket)
            basket_item = BasketItem.objects.get(product_version_id = product, basket_id = basket)
            basket_item.quantity += quantity
            if basket_item.quantity >= basket_item.product_version_id.quantity:
                message = {'success' : False, 'message': 'Choose a proper amount!'}
                return Response(message)
            basket_item.save()
            return Response(status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, *args, **kwargs):
        ProductID = request.data.get('product')
        if ProductID:
            user_basket = BasketItem.objects.get(id = ProductID, basket_id__user_id = request.user)
            user_basket.delete()
        return Response(status = status.HTTP_200_OK)
