from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('transaksi/', views.transaksi),
	path('input/', views.input),
	path('create/', views.sale_detail),
	# path('<kode_t>/kode', views.show_kode),
	path('<resi>/', views.show_detail),
	path('<id>/delete', views.delete),
	# path('<id>/update', views.update),
	path('<id>/detail', views.detail),
	path('<id>/detail/<id_detail>/delete', views.delete_detail),
]