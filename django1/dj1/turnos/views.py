from django.shortcuts import render
from turnos.models import *
# Create your views here.

from django.http import HttpResponse
from django.template import loader

#la siguiente view me muestra para un cliente determinado un mensaje de bienvenida y el menu de opciones
def homecli(request,idcli):
	cli= Cliente.objects.get(id=idcli)
	temp = loader.get_template("homecli.html")
	context = {"nombrecli":cli.nombre,"apellidocli":cli.apellido,"idcli":idcli}
	return HttpResponse(temp.render(context))

<<<<<<< HEAD
#la siguiente view me muestra para un cliente determinado todos los turnos que tiene asignados actualmente
def get_turnoscli(request,idcli):
	turnos = Turno.objects.all().filter(idcliente=idcli)
	temp = loader.get_template("turnoscli.html")
	context = {"turnos":turnos}
	return HttpResponse(temp.render(context))
=======

def layoutview(request):
	temp = loader.get_template("layout.html")
	context = {"Holi":"guacho"}
	return HttpResponse(temp.render(context))


def homeuserview(request):
	temp = loader.get_template("homeuser.html")
	context = {"Holi":"guacho"}
	return HttpResponse(temp.render(context))


	
>>>>>>> front_dev
