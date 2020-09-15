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

#a ver si anduvo gitignore 2do intetno 3intento algo masssss
class Turno(models.Model):
	idcliente = models.ForeignKey(Cliente,on_delete=models.CASCADE,null=True,blank=True)
	idproveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
	fecha_turno = models.DateTimeField(null=False,blank=False)
	fecha_solicitud = models.DateTimeField(null=True,blank=True)



