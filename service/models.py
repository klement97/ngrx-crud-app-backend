from django.db import models


class SCAModel(models.Model):
    app_label = 'CarWash'
    abstract = True


class Shop(SCAModel):
    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'
        db_table = 'shop'

    name = models.CharField(max_length=50, blank=False, null=False)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class ServiceType(SCAModel):
    class Meta:
        verbose_name = 'Service Type'
        verbose_name_plural = 'Service Types'
        db_table = 'service_type'
        ordering = ['-id']

    name = models.CharField(max_length=50, blank=False, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return self.name


class Service(SCAModel):
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        db_table = 'service'
        ordering = ['-date_created', '-time_created']

    date_created = models.DateField(auto_now_add=True)
    time_created = models.TimeField(auto_now_add=True)
    license_plate = models.CharField(max_length=15, blank=False, null=False)
    shop_id = models.ForeignKey(Shop, on_delete=models.PROTECT, verbose_name="Shop")
    service_type_id = models.ForeignKey(ServiceType, related_name='services', on_delete=models.PROTECT, verbose_name="Service Type")

    def __str__(self):
        return 'Service {}'.format(self.id)
