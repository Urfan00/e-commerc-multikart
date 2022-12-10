import django_filters.rest_framework
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from products.models import Brand, Category, Color, ProductVersion, Products, Size
from products.api.serializers import BrandCreateSerializer, BrandReadSerializer, CategorySerializer, ColorSerializer, ProductCreateSerializer, ProductReadSerializer, ProductVersionCreateSerializer, ProductVersionReadSerializer, SizeSerializer
from rest_framework.response import Response



# class BrandAPI(APIView):

#     def get(self, request, *args, **kwargs):
#         brands = Brand.objects.all()
#         serializer = BrandReadSerializer(brands, context = {'request' : request}, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializers = BrandCreateSerializer(data=request.data, context = {'request' : request})
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=201)
#         return Response(serializers.errors, status=400)


# class BrandReadUpdateDeleteView(APIView):

#     def get(self, request, *args, **kwargs):
#         id = kwargs['pk']
#         brand = Brand.objects.get(id=id)
#         serializer = BrandReadSerializer(brand)
#         return Response(serializer.data, status=200)

#     def put(self, request, *args, **kwargs):
#         id = kwargs['pk']
#         brand = Brand.objects.get(id=id)
#         brand_data = request.data
#         serializer = BrandCreateSerializer(data=brand_data, instance=brand)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=200)

#     def patch(self, request, *args, **kwargs):
#         id = kwargs['pk']
#         brand = Brand.objects.get(id=id)
#         brand_data = request.data
#         serializer = BrandCreateSerializer(data=brand_data, partial=True , instance=brand)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=200)

#     def delete(self, request, *args, **kwargs):
#         id = kwargs['pk']
#         brand = Brand.objects.get(id=id)
#         brand.delete()
#         return Response(status=204)


# ***************************genericview*******************************************


class GenericAPIViewSerializerMixin:
    def get_serializer_class(self):
        return self.serializer_classes[self.request.method]


class ProductAPI(GenericAPIViewSerializerMixin, ListCreateAPIView):
    queryset = Products.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category_id', 'brand_id']
    search_fields = ['name']
    serializer_classes = {
        'GET' : ProductReadSerializer,
        'POST' : ProductCreateSerializer
    }


class ProductReadUpdateDeleteView(GenericAPIViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_classes = {
        'GET' : ProductReadSerializer,
        'PUT' : ProductCreateSerializer,
        'PATCH' : ProductCreateSerializer
    }


class ProductVersionAPI(GenericAPIViewSerializerMixin, ListCreateAPIView):
    queryset = ProductVersion.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['product_id__category_id', 'product_id__brand_id', 'size_id', 'color_id']
    search_fields = ['product_id__product_name']
    serializer_classes = {
        'GET' : ProductVersionReadSerializer,
        'POST' : ProductVersionCreateSerializer
    }


class ProductVersionReadUpdateDeleteView(GenericAPIViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = ProductVersion.objects.all()
    serializer_classes = {
        'GET' : ProductVersionReadSerializer,
        'PUT' : ProductVersionCreateSerializer,
        'PATCH' : ProductVersionCreateSerializer
    }


class CategoryAPI(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = []
    search_fields = ['category_name']


class CategoryReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandAPI(GenericAPIViewSerializerMixin, ListCreateAPIView):
    queryset = Brand.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category_id']
    search_fields = ['name']
    serializer_classes = {
        'GET' : BrandReadSerializer,
        'POST' : BrandCreateSerializer
    }


class BrandReadUpdateDeleteView(GenericAPIViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_classes = {
        'GET' : BrandReadSerializer,
        'PUT' : BrandCreateSerializer,
        'PATCH' : BrandCreateSerializer
    }


class SizeAPI(ListCreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = []
    search_fields = ['name']


class SizeReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class ColorAPI(ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = []
    search_fields = ['name']


class ColorReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
