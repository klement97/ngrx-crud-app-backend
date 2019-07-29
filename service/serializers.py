from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Service, ServiceType, Shop


class ServiceListSerializer(ModelSerializer):
    shop_id = serializers.SerializerMethodField()
   # service_types = serializers.SerializerMethodField()
    date_created = serializers.SerializerMethodField()
    time_created = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = '__all__'

    @staticmethod
    def get_shop_id(obj):
        return obj.shop_id.name

#    @staticmethod	
 #   def get_service_types(obj):
  #      return obj.service_types.name

    @staticmethod
    def get_date_created(obj):
        return obj.date_created.strftime('%d/%m/%Y')

    @staticmethod
    def get_time_created(obj):
        return obj.time_created.strftime('%H:%m')


class ServiceSerializer(ModelSerializer):
    shop_id = serializers.SerializerMethodField()
    date_created = serializers.SerializerMethodField()
    time_created = serializers.SerializerMethodField()
    service_types = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = '__all__'

    @staticmethod
    def get_shop_id(obj):
        return obj.shop_id.name

    @staticmethod
    def get_service_types(obj):
        service_types = []
        types = ServiceTypeSerializer(obj.service_types, many=True).data
        for i in types:
            service_types.append(i['name'])
        return service_types

    @staticmethod
    def get_date_created(obj):
        return obj.date_created.strftime('%d/%m/%Y')

    @staticmethod
    def get_time_created(obj):
        return obj.time_created.strftime('%H:%m')


class ServiceTypeSerializer(ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ['id', 'name', 'price']
        extra_kwargs = {'id': {'read_only': True}}


class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
