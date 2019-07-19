from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Service, ServiceType, Shop


class ServiceSerializer(ModelSerializer):
    shop_id = serializers.SerializerMethodField()
    service_type_id = serializers.SerializerMethodField()
    time_created = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = '__all__'

    @staticmethod
    def get_shop_id(obj):
        return obj.shop_id.name

    @staticmethod
    def get_service_type_id(obj):
        return obj.service_type_id.name

    @staticmethod
    def get_time_created(obj):
        return obj.time_created.strftime('%H:%m')


class ServiceTypeSerializer(ModelSerializer):
    class Meta:
        model = ServiceType
        fields = '__all__'


class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
