from django.urls import path

from . import views

urlpatterns = [
    path('flights', views.flights, name="flights"),
    path('passengers', views.passengers, name="passengers")
]