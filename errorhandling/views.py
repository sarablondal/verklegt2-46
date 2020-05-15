from django.shortcuts import render

# Create your views here.

#View sem redirect-ar í error vefsíður okkar þegar ákveðinn error er trigger-að
def view_400(request, exception):
    return render(request, 'errors/400.html')

def view_403(request, exception):
    return render(request, 'errors/403.html')

def view_404(request, exception):
    return render(request, 'errors/404.html')

def view_500(request):
    return render(request, 'errors/500.html')