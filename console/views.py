from django.shortcuts import render, get_object_or_404

from console.forms.consoleForm import consoleCreateForm
from console.models import Console


# Create your views here.

def consoleIndex(request):
    context = {'consoles': Console.objects.all()}  #order_by('name')
    return render(request, 'catalog/consoleIndex.html', context)

# sækir gögn fyrir tiltekið console url, t.d. localhost:3000/consoles/3
def getConsoleById(request, id):
    return render(request, 'catalog/consoleDetails.html', {
        'console': get_object_or_404(Console, pk=id)
    })


def createConsole(request):
    if request.method == 'POST':
        print(1)
    else:
        form = consoleCreateForm()
    return render(request, 'catalog/createConsole.html', {
        'form': form
    })
