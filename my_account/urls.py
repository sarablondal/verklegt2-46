from django.urls import path
from . import views


urlpatterns = [
    #http://localhost:8000/my_account
    path('', views.index, name= "my_accountindex")
]