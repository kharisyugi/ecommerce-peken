from django.shortcuts import render, redirect
from . import models
# Create your views here.
def index(req):
	sppli = models.Supp.objects.all()
	return render(req, 'suppliers/index.html', {
		'data' : sppli,
		})

def input(req):
	if req.POST:
		models.Supp.objects.create(
			name = req.POST['name'],
			phone = req.POST['phone'],
			addrs = req.POST['addrs'],
			desc = req.POST['desc'])
		return redirect('/supplier')

	sppli = models.Supp.objects.all()
	return render(req, 'suppliers/input.html', {
		'data' : sppli,
		})

def update(req, id):
	if req.POST:
		models.Supp.objects.filter(pk=id).update(
			name = req.POST['name'],
			phone = req.POST['phone'],
			addrs = req.POST['addrs'],
			desc = req.POST['desc'])
		return redirect('/suppliers')

	sppli = models.Supp.objects.filter(pk=id).first()
	return render(req, 'suppliers/update.html', {
		'data' : sppli,
		})

def delete(req, id):
	models.Supp.objects.filter(pk=id).delete()
	return redirect('/suppliers')