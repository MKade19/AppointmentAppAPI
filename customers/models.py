from django.db import models

class Customer(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)