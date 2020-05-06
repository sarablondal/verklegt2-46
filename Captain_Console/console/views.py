from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #þessu verður svo breytt seinna, mkundi ekki hvernig ég gerði hitt atm en fínt að hafa í grunninn bara :)
    return HttpResponse("<h1>Hello form the index view in the  console app<h1>")