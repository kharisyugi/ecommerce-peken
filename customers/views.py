from django.shortcuts import render, redirect
from . import models

def index(req):
	cust = models.Cust.objects.all()
	return render(req, 'customers/index.html', {
		'data' : cust,
		})

def input(req):
	if req.POST:
		models.Cust.objects.create(
			name = req.POST['name'],
			phone = req.POST['phone'],
			addrs = req.POST['addrs'],
			gender = req.POST['gender'])
		return redirect('/customers')

	cust = models.Cust.objects.all()
	return render(req, 'customers/input.html', {
		'data' : cust,
		})

def update(req, id):
	if req.POST:
		models.Cust.objects.filter(pk=id).update(
			name = req.POST['name'],
			phone = req.POST['phone'],
			addrs = req.POST['addrs'],
			gender = req.POST['gender'])
		return redirect('/customers')

	cust = models.Cust.objects.filter(pk=id).first()
	return render(req, 'customers/update.html', {
		'data' : cust,
		})

def delete(req, id):
	models.Cust.objects.filter(pk=id).delete()
	return redirect('/customers')