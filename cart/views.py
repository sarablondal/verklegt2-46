from django.shortcuts import render

# Create your views here.

def cartIndex(request):
    return render(request, "purchase/cart/../templates/purchase/cart.html")