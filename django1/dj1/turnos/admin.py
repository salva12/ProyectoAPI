from django.contrib import admin
from turnos.models import *

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id','dni','apellido','tel')

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id','cuit','nombre','tel','rubro')

class TurnosAdmin(admin.ModelAdmin):
    list_display = ('id','idcliente','idproveedor','turno','fecha','hora')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Turno, TurnosAdmin)