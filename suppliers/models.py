from django.db import models

# Create your models here.
class Supp(models.Model):
	name = models.TextField(default='')
	phone = models.TextField(default='')
	addrs = models.TextField(default='')
	desc = models.TextField(default='')