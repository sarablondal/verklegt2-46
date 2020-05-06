from django.shortcuts import render
from console.models import Console

# Create your views here.

def index(request):
    context = {'consoles': Console.objects.all()}  #order_by('name')
    return render(request, 'catalog/index.html', context)

# sækir gögn fyrir tiltekið console url, t.d. localhost:3000/consoles/3
#def getConsoleById(request, id):
 #   return render(request, 'catalog/consoleDetails.html')

