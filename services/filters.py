import django_filters 
from . models import Query
class QueryFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    date_of_creation = django_filters.DateRangeFilter(label = 'Date')
    admitted_year = django_filters.CharFilter(lookup_expr="icontains")
    class Meta:
        model = Query
        fields = ['department','status']
        