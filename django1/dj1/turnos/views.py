from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def agendaview(request):
	temp = loader.get_template("agenda.html")
	context = {"tabla":"t1 t2 t3 ...."}
	return HttpResponse(temp.render(context))


def layoutview(request):
	temp = loader.get_template("layout.html")
	context = {"Holi":"guacho"}
	return HttpResponse(temp.render(context))


def homeuserview(request):
	temp = loader.get_template("homeuser.html")
	context = {"Holi":"guacho"}
	return HttpResponse(temp.render(context))


	