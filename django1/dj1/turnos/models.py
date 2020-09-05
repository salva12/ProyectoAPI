from django.db import models

# Create your models here.

class Cliente(models.Model):
	dni = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
	mail = models.EmailField(max_length=30)

class Proveedor(models.Model):
	cuit = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
	mail = models.EmailField(max_length=30)
    descrpcion= models.CharField(max_length=30)
    rubro= models.CharField(max_length=30)

