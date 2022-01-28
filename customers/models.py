from django.db import models

# Create your models here.
class Cust(models.Model):
	name = models.TextField(default='')
	gender = models.TextField(default='')
	phone = models.TextField(default='')
	addrs = models.TextField(default='')

	def __str__(self):
		return self.name