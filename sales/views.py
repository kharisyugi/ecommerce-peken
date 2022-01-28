from django.shortcuts import render,redirect
from products import models as products_models
from . import models, forms
from toko import models as toko_models
from django.http import JsonResponse, HttpResponse 
import json
from django.forms.models import model_to_dict
from pos.auth import check_token
import random
import string

def index(req):
		sale = models.Sale.objects.all()
		saledetailbyid = [] # merubah array versi django mjd array biasa
		for p in sale:
			saledetailbyid.append(model_to_dict(p))
		return JsonResponse({'data': saledetailbyid})



def show_detail(req, resi):#id 
	if req.method == 'GET':
		try:
			sale1 = models.Sale.objects.filter(sama__resi=resi).first()
			sale2 = models.Sale.objects.filter(kode_t=resi).first()
			sale_dict= {
				'orders': [],
			}
			if sale1 is not None:
				sd = model_to_dict(sale1)
				sd['orders'] = []
				for s in sale1.sama.filter(resi=resi):
        
					sd['orders'].append({
						'toko': model_to_dict(toko_models.Toko.objects.filter(id=s.toko.pk).first()),
						'products': model_to_dict(products_models.Prod.objects.filter(id=s.products.pk).first())
					})
				sale_dict['orders'].append(sd)
			elif sale2 is not None:
				sd = model_to_dict(sale2)
				sd['orders'] = []
				for s in sale2.sama.filter(sale__kode_t=resi):

					sd['orders'].append({
						'toko': model_to_dict(toko_models.Toko.objects.filter(id=s.toko.pk).first()),
						'products': model_to_dict(products_models.Prod.objects.filter(id=s.products.pk).first())
					})
				sale_dict['orders'].append(sd)
			return JsonResponse(sale_dict)
		except Exception as e:
			print('error => ', e)
			return JsonResponse({})



def random_numeric(size=10):
	chars = string.digits
	result = ''.join((random.choice(chars) for i in range(size) ))
	return result

def sale_detail(req):
	if req.method == 'POST':
		data_byte = req.body
		data_string = str(data_byte, 'utf-8')
		data = json.loads(data_string)
		kode = models.Kode.objects.create(uniq=int(data['uniqq']))#create isi data untuk pengurangan harga
		kode_t =random_numeric(10)# Unik pada kode transaki, 
		sale = models.Sale.objects.create(
			nama=data['nama'],
			email=data['email'],
			alamat=data['alamat'],
			no_hp=data['no_hp'],
			pengiriman=data['pengiriman'],
			provinsi=data['provinsi'],
			kabupaten=data['kabupaten'],
			kecamatan=data['kecamatan'],
			desa=data['desa'],
			uniqq=kode,
			kode_t=kode_t,
		)
			#return Json
		for order in data['orders']:
			detailbyprod = products_models.Prod.objects.filter(pk=order['products']).first()
			form = forms.SaleDetail(order)
			if form.is_valid():
				form.instance.sale = sale
				form.instance.products = detailbyprod
				form.instance.toko=detailbyprod.toko
				sd=form.save()
			else:
				print(form.errors)

		saledetail=models.SaleDetail.objects.filter(sale=sale)
		sale = model_to_dict(sale)
		sale['uniqq'] = kode.uniq
		sale['orders'] = []
		tokos = []
		total=0
		for t in saledetail:
			total+=t.total()
			tokos.append(t.toko.id)

		tokos = list(set(tokos))
		for toko_id in tokos:
			toko = toko_models.Toko.objects.filter(pk=toko_id).first()
			toko = model_to_dict(toko)
			resi = random_numeric(10) #uniq pada kode pertoko 
			toko['products'] = []
			sale_items = models.SaleDetail.objects.filter(toko=toko['id'], sale=sale['id'])
			toko['total'] = 0
			toko['resi'] = resi

			for sale_yes in sale_items:
				models.SaleDetail.objects.filter(id=sale_yes.id).update(resi=resi)
				sale_item = models.SaleDetail.objects.filter(id=sale_yes.id).first()
				toko['total'] += sale_item.total() #total pertoko
				sale_item_dict = model_to_dict(sale_item)
				sale_item_dict['products'] = model_to_dict(products_models.Prod.objects.filter(id=sale_item.products.id).first())
				toko['products'].append(sale_item_dict)
			toko['total'] -= kode.uniq
			sale['orders'].append(toko)
		return JsonResponse({
			'total': total - kode.uniq,
			'sale': sale,
		})
  
  
  ##BAGIAN SAMPAH##

def transaksi(req):
	# tasks = models.Sale.objects.filter(owner=req.user)
	sale = models.Sale.objects.all()
	total =0
	for p in sale:
		total+=p.total()

	return render(req, ('transaksi/list_transaksi.html'), {
		'data' : sale,
		'total': total,
		# 'data' : tasks,
		})

def input(req):
	# tasks = models.Sale.objects.filter(owner=req.user)
	form = forms.SalesForm()

	if req.POST:
		form = forms.SalesForm(req.POST)
		if form.is_valid():
			form.instance.owner = req.user
			form.save()
		
		return redirect('/sales')

	sale = models.Sale.objects.all()
	return render(req, ('sales/input.html'), {
		'data' : sale,
		'form' : form,
		'data' : tasks,
		})

	
def delete(req, id):
	models.Sale.objects.filter(pk=id).delete()
	return redirect('/sales')

def detail(req, id):
	sale = models.Sale.objects.filter(pk=id).first()
	saledetail=models.SaleDetail.objects.filter(sale=sale)
	return render(req, 'sales/detail.html', {
		'data': sale,
		'datadetail': saledetail,
		})

def delete_detail(req,id,id_detail):
	models.SaleDetail.objects.filter(pk=id_detail).delete()
	# stok_detail = products.stok+qty
	# products_models.Prod.objects.filter(pk=sale.products.id).update(stok=stok_detail)
	return redirect(f'/sales/{id}/detail')



		
	
# def show_kode(req, kode_t):# invoice Global
# 	if req.method =='GET':
# 		sale = models.Sale.objects.filter(kode_t=kode_t).first()
# 		# saledetail = models.SaleDetail.objects.filter(resi=resi).first()
# 		sale_dict = model_to_dict(sale)
# 		sale_dict['orders'] = []
# 		for z in sale.sama.all():
# 			z= model_to_dict(z)
# 			z['toko'] = model_to_dict(toko_models.Toko.objects.filter(id=z['toko']).first())
# 			z['products'] = model_to_dict(products_models.Prod.objects.filter(id=z['products']).first())
# 			sale_dict['orders'].append(z)
# 		return JsonResponse(sale_dict)
