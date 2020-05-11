from django.urls import path
from . import views


urlpatterns = [
    #http://localhost:8000/other
    path('', views.index, name= "otherindex"),
]