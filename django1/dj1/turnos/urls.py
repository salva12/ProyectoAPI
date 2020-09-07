from django.contrib import admin
from django.urls import path
from turnos import views

urlpatterns = [
    path('homecliente/<int:idcli>', views.homecli),
    path('homecliente/misturnos/<int:idcli>',views.get_turnoscli),
]
