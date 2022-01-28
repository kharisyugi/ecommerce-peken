from django.db import models
class Login1(models.Model):
    username = models.CharField(max_length =100)
    password = models.CharField(max_length=8)

    




