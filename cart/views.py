from django.shortcuts import render

# Create your views here.

def cartIndex(request):
    return render(request, "cart/../templates/purchase/cart.html")