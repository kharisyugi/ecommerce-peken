from django.db import models
from datetime import datetime
from products import models as products_models
from toko import models as toko_models
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
# Create your models here.
class Kode(models.Model):
    uniq = models.CharField(max_length=30)
class Sale(models.Model):
	nama = models.CharField(default='', max_length=30)
	email = models.TextField(default='', max_length=255)
	alamat = models.TextField(default='', max_length=255)
	no_hp = models.CharField(max_length=30)
	pengiriman = models.CharField(max_length=30)
	provinsi = models.CharField(default='', max_length=30)
	kabupaten = models.CharField(default='', max_length=30)
	kecamatan = models.CharField(default='', max_length=30)
	desa = models.CharField(default='', max_length=30)
	uniqq= models.ForeignKey(Kode,on_delete= models.CASCADE, related_name='harga1')
	kode_t =models.CharField(max_length=50)
 
 
	date = models.DateField(default=datetime.now)

	def total(self):
		details = SaleDetail.objects.filter(sale=self.id)
		total_price = 0
		for detail in details:
			total_price += detail.total()
		return total_price - self.uniqq.uniq
	
class SaleDetail(models.Model):	
	sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='sama')
	products = models.ForeignKey(products_models.Prod, on_delete=models.CASCADE, related_name='terjual') 
	toko = models.ForeignKey(toko_models.Toko,on_delete=models.CASCADE, related_name='penjualan') 
	qty = models.PositiveSmallIntegerField(default=0)
	resi =models.CharField(max_length=30)
	status =models.IntegerField(default=0)



	def __repr__(self):
		return '{} {} {}'.format(self.products, self.qty, self.products.stok)
		
	def total(self):
		return self.qty*self.products.price

	# def stok(self):
	# 	return self.products.stok-self.qty4 


