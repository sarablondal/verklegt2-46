from django.shortcuts import render

#taka þetta út þegar gögn eru komin í gagnagrunninn okkar
consoles = [
    {'name': 'Super mario', 'description': 'Leikur character sem er að bjarga prinsessu', 'company': 'Nintendo', 'price': 9.99}
]

# Create your views here.

def index(request):
    return render(request, 'catalog/index.html', context={'consoles':consoles})