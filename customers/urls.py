from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('input/', views.input),
	path('<id>/delete', views.delete),
	path('<id>/update', views.update),
]