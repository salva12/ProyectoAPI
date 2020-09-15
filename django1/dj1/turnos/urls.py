from django.contrib import admin
from django.urls import path
from turnos import views

urlpatterns = [
<<<<<<< HEAD
    path('homecliente/<int:idcli>', views.homecli),
    path('homecliente/misturnos/<int:idcli>',views.get_turnoscli),
=======
    path('agenda/', views.agendaview),
    path('layout/' , views.layoutview),
    path('homeuser/', views.homeuserview),
>>>>>>> front_dev
]
