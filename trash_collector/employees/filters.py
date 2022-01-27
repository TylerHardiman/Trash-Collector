import django_filters 

from .models import *

class OrderFilter(django_filters.FiltersSet):
  class Meta:
    model = Order
    fields = '__all__'