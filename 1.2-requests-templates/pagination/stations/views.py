from django.core import paginator
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from csv import DictReader


def index(request):
    return redirect(reverse('bus_stations'))

def get_bus_stations():
    with open(r'C:\Users\evgor\Desktop\dj-homeworks\1.2-requests-templates\pagination\data-398-2018-08-30.csv',
              'r', encoding='UTF-8') as file:
        return list(DictReader(file))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    all_stations = get_bus_stations()  # Read fresh data each request
    paginator = Paginator(all_stations, 10)
    page = paginator.get_page(page_number)

    context = {
        'page': page,
    }
    return render(request, 'stations/index.html', context)
