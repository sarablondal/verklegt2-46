from django.urls import path
from . import views, utils


urlpatterns = [
	#Leave as empty string for base url
	path('', views.cart, name="cart"),
	path('store/', views.cart, name="store"),
	#path('t', views.test, name="test"),
	path('updateitem/', views.updateItem, name="updateItem"),


	path('checkout/', views.checkout, name="checkout"),
	path('checkout2/', views.checkout2, name="checkout2"),

	path('process_order/', views.processOrder, name="process_order"),
]