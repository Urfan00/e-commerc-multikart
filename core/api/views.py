from rest_framework import generics
from core.models import Subscribe
from .serializers import SubscriberEmailSerializer


class SubscriberEmailView(generics.ListCreateAPIView):
    serializer_class = SubscriberEmailSerializer
    queryset = Subscribe.objects.all()
