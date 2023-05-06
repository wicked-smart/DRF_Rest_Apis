from django.shortcuts import render
from .models import *
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from .serializers import *

# Create your views here.

@api_view(['GET'])
def flights(request):

    if request.method == 'GET':

        flights = Flight.objects.all()
        
        serializer = FlightSerializer(flights, many=True)
        return JsonResponse(serializer.data, safe=False)

   
@api_view(['GET'])
def passengers(request):

    if request.method == 'GET':

        passengers = Passenger.objects.all()
        serializer= PassengerSerializer(passengers, many=True)
        return JsonResponse(serializer.data, safe=False)
