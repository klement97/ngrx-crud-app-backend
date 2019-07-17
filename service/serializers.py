from rest_framework.serializers import ModelSerializer
from .models import Service, ServiceType, Shop


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceTypeSerializer(ModelSerializer):
    class Meta:
        model = ServiceType
        fields = '__all__'


class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
