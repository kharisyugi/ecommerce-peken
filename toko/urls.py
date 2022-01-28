from django.urls import path
from . import views

urlpatterns = [
	path('<id>/', views.detail_toko),
	path('create/', views.create),
	path('<id>/delete', views.delete),
	path('sale/', views.sale),
	path('',views.index),

]