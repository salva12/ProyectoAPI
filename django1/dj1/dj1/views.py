from django.http import HttpResponse
from django.template import loader

def homeview(request):
	temp = loader.get_template("home.html")
	context = {"campo_msjinicio":"Dj1 es una plataforma web genial"}
	return HttpResponse(temp.render(context))


