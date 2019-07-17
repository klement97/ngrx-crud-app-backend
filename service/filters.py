from django.forms import DateInput
from django_filters import FilterSet, CharFilter, DateFilter

from .models import Service


class ServiceFilter(FilterSet):
    license_plate = CharFilter(lookup_expr='icontains')
    # shop_id = ChoiceFilter(queryset=Shop.objects.all(), widget=Select(attrs={'class': 'form-control form-control-sm'}))
    date_created = DateFilter(
        widget=DateInput(
            attrs={
                'class': 'datepicker',
                'type': 'date'
            }
        )
        , field_name='date_created')

    # date_min = DateFromToRangeFilter()

    class Meta:
        model = Service
        fields = ['shop_id', 'service_type_id', 'date_created', 'license_plate']
