from django.urls import path
from . import views


urlpatterns = [
	#Leave as empty string for base url
	path('', views.cart, name="cart"),
	path('', views.cart, name="store"),

	path('checkout/', views.checkout, name="checkout"),
	path('checkout2/', views.checkout2, name="checkout2"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
]