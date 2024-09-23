from rest_framework import serializers
from flightcards.models import Flight

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'  # O puedes especificar campos específicos en lugar de '__all__'
