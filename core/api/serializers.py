from rest_framework import serializers
from core.models import Subscribe


class SubscriberEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ['id', 'email']
