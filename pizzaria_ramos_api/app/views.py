from pizzaria_ramos_api.app.models import Pizza
from pizzaria_ramos_api.app.serializers import PizzaSerializer
from rest_framework import viewsets, filters

# Create your views here.
class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
