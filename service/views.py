from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView

from carwash_backend.common.api_view import SCAPIViewListCreate
from .models import Service, ServiceType, Shop
from .serializers import ServiceSerializer, ServiceTypeSerializer, ShopSerializer, ServiceListSerializer


# Shop Views
class ShopListView(ListAPIView):
    model = Shop
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()


# Service Type Views
class ServiceTypeListApiView(ListAPIView):
    model = ServiceType
    serializer_class = ServiceTypeSerializer
    queryset = ServiceType.objects.all()


class ServiceTypeCreateApiView(CreateAPIView):
    model = ServiceType
    serializer_class = ServiceTypeSerializer
    queryset = ServiceType.objects.all()


class ServiceTypeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    model = ServiceType
    serializer_class = ServiceTypeSerializer
    queryset = ServiceType.objects.all()


# Service Views
class ServiceListApiView(SCAPIViewListCreate):
    model = Service
    serializer_class = ServiceListSerializer
    queryset = Service.objects.all()


class ServiceCreateApiView(CreateAPIView):
    model = Service
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class ServiceRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    model = Service
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
