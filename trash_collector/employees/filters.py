import django_filters 
from django_filters import DateFilter
from .models import Customer

class DayFilter(django_filters.FilterSet):
  # start_date = DateFilter(field_name='weekly_pickup', lookup_expr='gte')
  # end_date = DateFilter(field_name='one_time_pickup', lookup_expr='lte')
  class Meta:
    model = Customer
    fields = '__all__'
    exclude =  ['name', 'address', 'zip_code', 'suspend_start', 'suspend_end', 'date_of_last_pickup', 'balance', 'user_id']