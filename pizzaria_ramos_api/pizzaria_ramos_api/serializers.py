from rest_framework import serializers
from pizzaria_ramos_api.pizzaria_ramos_api.models import Pizza

class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pizza
        fields = ['url', 'id', 'name', 'ingredients', 'price']
