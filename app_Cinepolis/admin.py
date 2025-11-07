from django.contrib import admin
from .models import Sucursal, Sala, Pelicula

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('id_sucursal','nombre_cine','direccion','ciudad','telefono','numero_salas','estado','formatos')
    search_fields = ('nombre_cine','ciudad','direccion')
    list_filter = ('estado','formatos')

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('id_sala', 'numero_sala', 'tipo_sala', 'capacidad', 'estado', 'fecha_ultimo_mantenimiento', 'asientos_especiales', 'sucursal')
    list_filter = ('tipo_sala', 'estado', 'sucursal')
    search_fields = ('numero_sala',)

admin.site.register(Pelicula)  # pendiente usar
