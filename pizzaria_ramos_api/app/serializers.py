from rest_framework import serializers
from pizzaria_ramos_api.app.models import Pizza


class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pizza
        fields = [
            'url',
            'created',
            'id',
            'name',
            'ingredients',
            'price',
            'image_file',
            'image_text',
        ]
