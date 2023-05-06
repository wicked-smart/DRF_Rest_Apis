from rest_framework import serializers
from .models import *

class AirportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airport
        fields = ['city', 'code']

class FlightSerializer(serializers.ModelSerializer):
    origin = serializers.StringRelatedField()
    destination = serializers.StringRelatedField()

    class Meta:
        model = Flight
        fields = ['id', 'origin', 'destination', 'duration']

class PassengerSerializer(serializers.ModelSerializer):
    flight = serializers.StringRelatedField(many=True)

    class Meta:
        model = Passenger
        fields = ['id', 'first_name', 'last_name', 'flight']