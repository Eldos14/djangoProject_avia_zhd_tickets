from django.shortcuts import render
from django.http import HttpResponse
from .models import Ticket, City, Route
from django.db.models import Q

def home(request):
    return render(request, "main/index.html")  


def ticket_list(request):
    
    cities = City.objects.all()

   
    departure_id = request.GET.get('from')
    destination_id = request.GET.get('to')

    tickets = Ticket.objects.all()

    if departure_id and destination_id:
        tickets = tickets.filter(
            route__departure__id=departure_id,
            route__destination__id=destination_id
        )

    context = {
        'tickets': tickets,
        'cities': cities,
        'selected_from': departure_id,
        'selected_to': destination_id
    }
    return render(request, 'main/ticket_list.html', context)
