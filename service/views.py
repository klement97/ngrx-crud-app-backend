from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView

from carwash_backend.common.api_view import SCAPIViewListCreate
from .models import Service, ServiceType, Shop
from .serializers import ServiceSerializer, ServiceTypeSerializer, ShopSerializer, ServiceListSerializer


# Shop View
class ShopListView(ListAPIView):
    model = Shop
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()


# Service Type View
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


# Service View
class ServiceListApiView(SCAPIViewListCreate):
    model = Service
    serializer_class = ServiceListSerializer
    queryset = Service.objects.all()

    # def form_valid(self, form):
    #     form.save()
    #
    #     # getting required values from form
    #     price = str(form.cleaned_data['service_type_id'].price)
    #     shop_name = str(form.cleaned_data['shop_id'].name)
    #     service_type_name = str(form.cleaned_data['service_type_id'].service_name)
    #     license_plate = str(form.cleaned_data['license_plate'])
    #
    #     URL = 'http://192.168.0.129:5000/print'
    #     # URL = 'http://127.0.0.1:5000/print'
    #     data = {
    #         'shop_name': shop_name,
    #         'service_type_name': service_type_name,
    #         'price': price,
    #         'license_plate': license_plate
    #     }
    #     requests.post(url=URL, json=data)
    #     return HttpResponseRedirect(self.success_url)


class ServiceCreateApiView(CreateAPIView):
    model = Service
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class ServiceRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    model = Service
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
