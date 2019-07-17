from django.urls import path

from service.views import ServiceRetrieveUpdateDestroyApiView, ServiceTypeRetrieveUpdateDestroyAPIView, ShopListView, ServiceListApiView, \
    ServiceCreateApiView, ServiceTypeListApiView, ServiceTypeCreateApiView

app_label = 'service'
urlpatterns = [

    path('shops/', ShopListView.as_view()),

    path('service_types/', ServiceTypeListApiView.as_view()),

    path('service/', ServiceCreateApiView.as_view()),

    path('manager/service_types/', ServiceTypeListApiView.as_view()),

    path('manager/service_types/create/', ServiceTypeCreateApiView.as_view()),

    path('manager/service_types/<int:pk>/', ServiceTypeRetrieveUpdateDestroyAPIView.as_view()),

    path('manager/services', ServiceListApiView.as_view()),

    path('manager/service/<int:pk>', ServiceRetrieveUpdateDestroyApiView.as_view()),

    # path('redirect/', redirect_user, name='redirect'),
]
