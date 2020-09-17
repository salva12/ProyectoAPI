#Es el vistas del general, no necesitamos por ahora 15/09/2020
from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponse
from django.template import loader

def login(request):
    temp = loader.get_template("login.html")
    context = {"Holi":"mundo"}
    return HttpResponse(temp.render(context))




