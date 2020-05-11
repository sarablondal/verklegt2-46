from django.urls import path
from . import views


urlpatterns = [
    #http://localhost:8000/consoles_sale
    path('', views.index, name= "consoleSaleIndex"),
]