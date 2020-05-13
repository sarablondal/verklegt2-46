from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

import console
from console.forms.consoleForm import ConsoleCreateForm, ConsoleUpdateForm
from console.models import Console


# Create your views here.

def consoleIndex(request):
    if 'searchFilter' in request.GET:
        searchFilter = request.GET['searchFilter']
        consoles = [{
            'id': i.id,
            'name': i.name,
            'description': i.description,
            'company': i.company,
            'price': i.price,
            'firstImage': i.consoleimage_set.first().image
        } for i in Console.objects.filter(name__icontains=searchFilter)]

        return JsonResponse({'data': consoles})
    context = {'consoles': Console.objects.all()}  #order_by('name')
    return render(request, 'catalog/consoleIndex.html', context)

###########################################
def sortNameIndex(request):
    context = {'consoles': Console.objects.all().order_by('name')}  # order_by('name')
    return render(request, 'catalog/consoleIndex.html', context)

def sortPriceIndex(request):
    context = {'consoles': Console.objects.all().order_by('price')}  # order_by('price')
    return render(request, 'catalog/consoleIndex.html', context)
###########################################

# sækir gögn fyrir tiltekið console url, t.d. localhost:3000/consoles/3
def getConsoleById(request, id):
    return render(request, 'catalog/consoleDetails.html', {
        'console': get_object_or_404(Console, pk=id)
    })


def createConsole(request):
    if request.method == 'POST':
        print(1)
    else:
        form = ConsoleCreateForm()
    return render(request, 'catalog/createConsole.html', {
        'form': form
    })

def deleteConsole(request, id):
    console = get_object_or_404(Console, pk=id)
    console.delete()
    return redirect("consoleIndex")


def updateConsole(request, id):
    instance = get_object_or_404(Console, pk=id)
    if request.method == 'POST':
        form = ConsoleUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('consoleDetails', id=id)

    else:
        form = ConsoleUpdateForm(instance=instance)
    return render(request, 'catalog/updateConsole.html', {
        'form': form,
        'id': id
    })

