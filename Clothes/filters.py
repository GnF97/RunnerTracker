import django_filters
from django_filters import DateFilter, NumberFilter

from .models import *

class RunFilter(django_filters.FilterSet):
    mileage_F = NumberFilter(field_name="mileage",lookup_expr='gte')
    class Meta:
        model = Runs
        fields = '__all__'
        exclude = ['date','shoe', 'mileage']