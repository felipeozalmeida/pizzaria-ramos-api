from pizzaria_ramos_api.pizzaria_ramos_api.models import Pizza
from pizzaria_ramos_api.pizzaria_ramos_api.serializers import PizzaSerializer
from rest_framework import viewsets

# Create your views here.
class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
