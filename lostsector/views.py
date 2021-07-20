from django.shortcuts import render
from django.http import HttpResponse
from . import views, lost_sector

# Create your views here.
def index(request):
    return HttpResponse("This is the Vegeta Commands Site!")

def today_lost_sector(request):
    return HttpResponse(lost_sector.today_lost_sector())

def lost_sector_vegeta(request):
    return HttpResponse(lost_sector.today_lost_sector_vegeta())