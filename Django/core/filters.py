import django_filters
from core import models

class Tag(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name='id')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model = models.Tag
        exclude = ('active',)
        filter_fields = ['name',]
