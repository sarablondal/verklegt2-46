from django.urls import path
from . import views


urlpatterns = [
    #http://localhost:8000/about_us
    path('', views.index, name= "about_usindex"),
]