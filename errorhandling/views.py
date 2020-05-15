from django.shortcuts import render

# Create your views here.
def view_400(request, exception):
    return render(request, 'errors/400.html')

def view_403(request, exception):
    return render(request, 'errors/403.html')

def view_404(request, exception):
    return render(request, 'errors/404.html')

def view_500(request):
    return render(request, 'errors/500.html')