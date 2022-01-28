from django.db import models
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.db.models.fields.files import ImageFieldFile


class Toko(models.Model):
    pemilik = models.ForeignKey(User, on_delete=models.CASCADE, related_name='toko')
    nama = models.CharField(default='', max_length=255)
    nomor_ktp= models.CharField(default='', max_length=255)
    nomor_rek= models.CharField(default='', max_length=255)
    nama_bank= models.CharField(default='', max_length=255)
    pemilik_bank = models.TextField(default='', max_length=255)
    alamat = models.TextField(default='', max_length=255)
    telp = models.CharField(default='',max_length=255)
    gambar = models.TextField(default='')
    
