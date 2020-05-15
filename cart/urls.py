from django.urls import path
from . import views, utils


urlpatterns = [
	#Leave as empty string for base url
	path('', views.cart, name="cart"),
	path('store/', views.cart, name="store"),
	#path('t', views.test, name="test"),
	path('view', views.updateItem, name="updateItem"),


	path('checkout/', views.checkout, name="checkout"),
	path('checkout2/', views.checkout2, name="checkout2"),
	path('checkout3/', views.checkout3, name="checkout3"),
	path('checkout4/', views.checkout4, name="checkout4"),


	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order")
]
