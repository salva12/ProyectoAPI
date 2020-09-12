from django.contrib import admin
from django.urls import path
from turnos import views

urlpatterns = [
    path('agenda/', views.agendaview),
    path('layout/' , views.layoutview),
    path('homeuser/', views.homeuserview),
]
