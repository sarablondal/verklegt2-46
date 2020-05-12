from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/consoles
    path('', views.consoleIndex, name="consoleIndex"),
    path('<int:id>', views.getConsoleById, name="consoleDetails"),
    path('createConsole', views.createConsole, name="createConsole"),
    path('deleteConsole/<int:id>', views.deleteConsole, name="deleteConsole"),
    path('updateConsole/<int:id>', views.updateConsole, name="updateConsole"),
    path('sortbyname', views.sortNameIndex, name = "sortByName"),
    path('sortbyprice', views.sortPriceIndex, name = "sortByPrice"),
    #sara
    path('', views.store, name="store"),
    path('store/', views.cart, name="store"),
    path('checkout/', views.checkout, name="checkout"),

]