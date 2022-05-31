from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    csvfile = open('data-398-2018-08-30.csv', newline='', encoding='utf-8')
    reader = csv.DictReader(csvfile)
    print(reader())
    for row in reader:
        print(row['Street'], row['District'])

    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
        'bus_stations': row,

    }
    return render(request, 'stations/index.html', context)
