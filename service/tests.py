from django.db.models import ProtectedError
from django.test import Client, TestCase
from django.urls import reverse
from service.models import Shop, ServiceType, Service
from django.contrib.auth.models import User


class TestIndexView(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create(username='admin', is_staff=True, is_active=True, is_superuser=True)
        user.set_password('12345')
        user.save()
        self.shop = Shop.objects.create(name='Special Car Wash',
                                        address='Street', user_id=user.id)

    def test_index_view(self):

        url = reverse('shop')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        # self.assertEqual(len(response.context['shops']), 1)

        # shop = response.context['shops'][0]

        # self.assertEqual(shop.name, 'Special Car Wash')
        # self.assertEqual(shop.address, 'Street')


class TestServiceTypeListView(TestCase):

    def setUp(self):
        self.client = Client()

        self.service_type = ServiceType.objects.create(service_name='Inner Wash',
                                                       price=300.00)

    """def test_service_types_are_list(self):
        # test the request method GET
        url = reverse('index')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['service_types']), 1)
    """


class TestServiceTypeViewCRUD(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create(username='admin', is_staff=True, is_active=True, is_superuser=True)
        user.set_password('12345')
        user.save()
        self.client.login(username='admin', password='12345')

    def test_creation_of_service_type_object(self):
        post_data = {'name': 'Inner Wash', 'price': 300.00}
        response = self.client.post('/admin/service/servicetype/add/', post_data)
        self.assertEqual(response.status_code, 302)

    def test_update_of_service_type_object(self):
        service_type_obj = ServiceType.objects.create(service_name='Inner Wash', price=300.00)
        update_data = {'name': 'Inner Car Wash', 'price': 500.00}
        url = '/admin/service/servicetype/{}/change/'.format(service_type_obj.pk)
        response = self.client.post(url, update_data)

        self.assertEqual(response.status_code, 302)
        service_type_obj.refresh_from_db()
        self.assertEqual(service_type_obj.price, 500)
        self.assertEqual(service_type_obj.service_name, 'Inner Car Wash')


class TestServiceTypeUpdateView(TestCase):
    pass


class TestServiceTypeDeleteView(TestCase):
    pass


class TestServiceCreationView(TestCase):
    pass


class TestServiceDeleteView(TestCase):
    pass


class TestServiceUpdateView(TestCase):
    pass


class TestSerViceCRUDView(TestCase):
    def setUp(self):
        # self.normal_client = Client()
        self.client = Client()
        user = User.objects.create(username='admin', is_staff=True, is_active=True, is_superuser=True)
        user.set_password('12345')
        user.save()
        self.client.login(username='admin', password='12345')
        self.shop = Shop.objects.create(name="Special Car Wash", address="Street", user_id=user.id)
        self.service_type = ServiceType.objects.create(service_name="Inner", price=600.00)
        self.service = Service.objects.create(license_plate="012345F", shop_id=self.shop,
                                              service_type_id=self.service_type)

    def test_creation_of_service_object(self):
        post_data = {'shop_id': self.shop.id, 'service_type_id': self.service_type.id,
                     'license_plate': '0333'}
        response = self.client.post(reverse('create_service'), post_data)
        self.assertEqual(response.status_code, 302)

        # check if the new object has been created
        second_response = self.client.get(reverse('services'))
        self.assertEqual(len(second_response.context['services']), 2)

    def test_service_objects_are_listed(self):
        response = self.client.get(reverse('services'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['services']), 1)

        service = response.context['services'][0]

        self.assertEqual(service.shop_id, self.shop)
        self.assertEqual(service.service_type_id, self.service_type)
        self.assertEqual(service.license_plate, '012345F')
        self.assertEqual(service.service_type_id.price, 600.00)

    def test_service_object_is_updated(self):
        service = Service.objects.create(shop_id=self.shop, service_type_id=self.service_type,
                                         license_plate='0333')
        update_data = {'shop_id': self.shop.id, 'service_type_id': self.service_type.id, 'license_plate': '0444'}
        url = '/admin/service/service/{}/change/'.format(service.pk)
        response = self.client.post(url, update_data)

        self.assertEqual(response.status_code, 302)
        service.refresh_from_db()
        self.assertEqual(service.license_plate, '0444')

    def test_service_object_is_deleted(self):
        pass


class TestShopCRUDView(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create(username='admin', is_staff=True, is_active=True, is_superuser=True)
        user.set_password('12345')
        user.save()
        self.client.login(username='admin', password='12345')
        self.shop = Shop.objects.create(name='Car Wash', address='London', user_id=user.id)

    def test_shop_objects_are_listed(self):
        response = self.client.get(reverse('shop'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['shops']), 1)

        shop = response.context['shops'][0]
        self.assertEqual(shop.address, 'London')
        self.assertEqual(shop.name, 'Car Wash')


class TestManagerViews(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create(username='admin', is_staff=True, is_active=True, is_superuser=True)
        user.set_password('12345')
        user.save()
        self.client.login(username='admin', password='12345')
        self.shop = Shop.objects.create(name="Special Car Wash", address="Street", user_id=user.id)
        self.service_type = ServiceType.objects.create(service_name="Inner", price=600.00)
        self.service = Service.objects.create(license_plate="012345F", shop_id=self.shop,
                                              service_type_id=self.service_type)

    def test_manager_can_view_service_types(self):
        response = self.client.get(reverse('service_types'))
        service_types = response.context['list']
        service_type = service_types[0]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(service_types), 1)
        self.assertEqual(service_type.service_name, 'Inner')
        self.assertEqual(service_type.price,  600.00)

    def test_manager_can_view_services(self):
        response = self.client.get(reverse('services'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['services']), 1)

        service = response.context['services'][0]

        self.assertEqual(service.shop_id, self.shop)
        self.assertEqual(service.service_type_id, self.service_type)
        self.assertEqual(service.license_plate, '012345F')
        self.assertEqual(service.service_type_id.price, 600.00)

    def test_manager_can_create_service_type(self):
        post_data = {'service_name': 'InOut', 'price': 1300.00}
        response = self.client.post(reverse('create_stype'), post_data)
        second_response = self.client.get(reverse('service_types'))
        service_type = second_response.context['list'][1]

        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(second_response.context['list']), 2)
        self.assertEqual(service_type.price, 1300.00)
        self.assertEqual(service_type.service_name, 'InOut')

    def test_manager_can_update_service_type(self):
        update_data = {'service_name': 'Outer', 'price': 800.00}
        response = self.client.post(reverse('edit_stype', kwargs={'pk': self.service_type.pk}),
                                    update_data)
        self.assertEqual(response.status_code, 302)

        second_response = self.client.get(reverse('service_types'))
        service_type = second_response.context['list'][0]
        self.assertEqual(len(second_response.context['list']), 1)
        self.assertEqual(service_type.price, 800.00)
        self.assertEqual(service_type.service_name, 'Outer')

    def test_manager_can_not_delete_service_types(self):
        try:
            self.client.delete(reverse('delete_stype', kwargs={'pk': self.service_type.pk}))
        except ProtectedError:
            pass

        second_response = self.client.get(reverse('service_types'))
        self.assertEqual(len(second_response.context['list']), 1)

    def test_manager_can_update_service(self):
        service = Service.objects.create(license_plate='0123', shop_id=self.shop,
                                         service_type_id=self.service_type)
        update_data = {'license_plate': '013', 'shop_id': self.shop.id,
                       'service_type_id': self.service_type.id}
        response = self.client.post(reverse('update_service', kwargs={'pk': service.pk}), update_data)
        second_response = self.client.get(reverse('services'))
        service = second_response.context_data['services'][0]

        self.assertEqual(response.status_code, 302)
        self.assertEqual(service.license_plate, '013')

    def test_manager_can_delete_service(self):
        response = self.client.delete(reverse('delete_service', kwargs={'pk': self.service.pk}))
        second_response = self.client.get(reverse('services'))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(second_response.context['services']), 0)


class TestCarWasherCRUD(TestCase):
    def setUp(self):
        self.service_type = ServiceType.objects.create(service_name="Inner", price=600.00)
        self.client = Client()
        self.car_washer = User.objects.create(username='car_washer', is_active=True)
        self.car_washer.set_password('12345')
        self.shop = Shop.objects.create(name="Special Car Wash", address="Street", user_id=self.car_washer.id)
        self.client.login(username='car_washer', password='12345')

    def test_car_washer_can_create_service(self):
        post_data = {'license_plate': '013', 'shop_id': self.shop.id, 'service_type_id': self.service_type.id}
        response = self.client.post(reverse('create_service'), post_data)
        self.assertEqual(response.status_code, 302)

    def test_car_washer_can_not_view_services(self):
        response = self.client.get(reverse('services'))
        self.assertEqual(response.status_code, 302)
