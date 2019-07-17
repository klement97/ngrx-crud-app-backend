from django.contrib import admin
from .models import Shop, Service, ServiceType


admin.site.register(Shop)
admin.site.register(ServiceType)
admin.site.register(Service)
