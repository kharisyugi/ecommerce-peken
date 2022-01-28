from django.urls import path
from . import views

urlpatterns = [
	path('', views.index), # ITEMS # ITEMS # ITEMS
	path('input_products/', views.input),
	path('category/', views.category),
	path('category/input_category/', views.input_c),
	path('<id>/delete', views.delete),
	path('category/<id>/delete', views.delete_c),
	path('<id>/update', views.update),
	path('<id>/show_b', views.show_b),
	path('<id>/show_detail', views.detail),
	# path('category/category/', views.category), # CATEGORY # CATEGORY # CATEGORY
	# path('category/input_category/', views.input_category),
	# path('category/<id>/delete', views.delete_category),
	# path('category/<id>/update', views.update_category),
	# path('units/units/', views.units), # UNIT # UNIT # UNIT
	# path('units/input/', views.input_u),
	# path('units/<id>/delete', views.delete_u),
	# path('units/<id>/update', views.update_u),
]