from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_cinepolis, name='inicio'),
    path('sucursal/agregar/', views.agregar_sucursal, name='agregar_sucursal'),
    path('sucursal/ver/', views.ver_sucursales, name='ver_sucursales'),
    path('sucursal/actualizar/<int:id_sucursal>/', views.actualizar_sucursal, name='actualizar_sucursal'),
    path('sucursal/realizar_actualizacion/<int:id_sucursal>/', views.realizar_actualizacion_sucursal, name='realizar_actualizacion_sucursal'),
    path('sucursal/borrar/<int:id_sucursal>/', views.borrar_sucursal, name='borrar_sucursal'),
    path('sala/agregar/', views.agregar_sala, name='agregar_sala'),
    path('sala/ver/', views.ver_sala, name='ver_sala'),
    path('sala/actualizar/<int:id_sala>/', views.actualizar_sala, name='actualizar_sala'),
    path('sala/realizar_actualizacion/<int:id_sala>/', views.realizar_actualizacion_sala, name='realizar_actualizacion_sala'),
    path('sala/borrar/<int:id_sala>/', views.borrar_sala, name='borrar_sala'),
]
