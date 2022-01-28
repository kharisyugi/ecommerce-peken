from django.shortcuts import render
from . import models, forms
from django.http import JsonResponse, HttpResponse
import json
from django.forms.models import model_to_dict
from toko import models as sales_models
from pos.auth import check_token

def detail_toko(req, id):
	toko = models.Toko.objects.filter(pk=id).first()
	penjualan = toko.penjualan.all()
	sale_penjualan = {'toko' : model_to_dict(toko) }
	sale_penjualan['penjualan'] = []
	try:
		for penj in penjualan:
			penj_d = model_to_dict(penj.sale)
			penj_d.update(model_to_dict(penj))
			penj_d['product']= model_to_dict(penj.products)
			sale_penjualan['penjualan'].append(penj_d)
		return JsonResponse(sale_penjualan)
	except Exception as e:
		print(e)
		return JsonResponse({})


def index(req):
	toko = models.Toko.objects.all()
	datatoko = []

	for t in toko:
		datatoko.append(model_to_dict(t))
	return JsonResponse({'toko' : datatoko,})

def create(req):
	# tasks = models.Prod.objects.filter(owner=req.user)
	form = forms.Toko()
	if req.method == 'POST':
		data_byte = req.body
		data_string = str(data_byte, 'utf-8')
		data = json.loads(data_string)
		form = forms.Toko(data)
		if form.is_valid():
			form.save()
	return JsonResponse({
		'datatoko' : model_to_dict(form.instance),
		})

def delete(req, id):
	delete = models.Toko.objects.filter(pk=id).delete()
	return JsonResponse({
		'toko' : delete,
		})

def sale(req):
	toko = models.Toko.objects.all()
	datatoko = []

	for t in toko:
		datatoko.append(model_to_dict(t))
	return JsonResponse({'toko' : datatoko,})







	
