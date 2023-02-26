from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Flight, Airport, Passenger


# Create your views here.

def index(request):
    return render(request, "src/flights.html", {
        "flights": Flight.objects.all()
    })


def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    passenger = flight.passengers.all()
    nonPassenger = Passenger.objects.exclude(flights=flight).all()
    return render(request, "src/flight.html", {
        "flight": flight,
        "passenger": passenger,
        "nonPassenger": nonPassenger,
    })


def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(id=flight_id)
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        passenger.flights.add(flight)

        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
