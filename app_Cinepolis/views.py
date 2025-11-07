from django.shortcuts import render, redirect, get_object_or_404
from .models import Sucursal, Sala

def inicio_cinepolis(request):
    return render(request, 'inicio.html')

def agregar_sucursal(request):
    if request.method == 'POST':
        # obtener datos del POST sin validación (según indicación)
        nombre = request.POST.get('nombre_cine')
        direccion = request.POST.get('direccion')
        ciudad = request.POST.get('ciudad')
        telefono = request.POST.get('telefono')
        numero_salas = request.POST.get('numero_salas') or 0
        estado = request.POST.get('estado') or 'activo'
        formatos = request.POST.get('formatos') or 'tradicional'

        suc = Sucursal(
            nombre_cine=nombre,
            direccion=direccion,
            ciudad=ciudad,
            telefono=telefono,
            numero_salas=int(numero_salas),
            estado=estado,
            formatos=formatos
        )
        suc.save()
        return redirect('ver_sucursales')

    return render(request, 'sucursal/agregar_sucursal.html')

def ver_sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursal/ver_sucursales.html', {'sucursales': sucursales})

def actualizar_sucursal(request, id_sucursal):
    suc = get_object_or_404(Sucursal, pk=id_sucursal)
    return render(request, 'sucursal/actualizar_sucursal.html', {'sucursal': suc})

def realizar_actualizacion_sucursal(request, id_sucursal):
    suc = get_object_or_404(Sucursal, pk=id_sucursal)
    if request.method == 'POST':
        suc.nombre_cine = request.POST.get('nombre_cine')
        suc.direccion = request.POST.get('direccion')
        suc.ciudad = request.POST.get('ciudad')
        suc.telefono = request.POST.get('telefono')
        suc.numero_salas = int(request.POST.get('numero_salas') or suc.numero_salas)
        suc.estado = request.POST.get('estado') or suc.estado
        suc.formatos = request.POST.get('formatos') or suc.formatos
        suc.save()
        return redirect('ver_sucursales')
    # si alguien entra por GET redirigimos al formulario de edición
    return redirect('actualizar_sucursal', id_sucursal=id_sucursal)

def borrar_sucursal(request, id_sucursal):
    suc = get_object_or_404(Sucursal, pk=id_sucursal)
    if request.method == 'POST':
        suc.delete()
        return redirect('ver_sucursales')
    return render(request, 'sucursal/borrar_sucursal.html', {'sucursal': suc})

# ---------- SALA ----------
def agregar_sala(request):
    # Cargar sucursales para el select
    sucursales = Sucursal.objects.all()

    if request.method == 'POST':
        numero_sala = request.POST.get('numero_sala')
        tipo_sala = request.POST.get('tipo_sala') or 'Tradicional'
        capacidad = request.POST.get('capacidad') or 0
        estado = request.POST.get('estado') or 'Desocupada'
        fecha_ultimo_mantenimiento = request.POST.get('fecha_ultimo_mantenimiento')
        asientos_especiales = request.POST.get('asientos_especiales') or 0
        sucursal_id = request.POST.get('sucursal_id')

        sala = Sala(
            numero_sala=int(numero_sala),
            tipo_sala=tipo_sala,
            capacidad=int(capacidad),
            estado=estado,
            fecha_ultimo_mantenimiento=fecha_ultimo_mantenimiento,
            asientos_especiales=int(asientos_especiales),
            sucursal=get_object_or_404(Sucursal, pk=sucursal_id)
        )
        sala.save()
        return redirect('ver_sala')

    return render(request, 'sala/agregar_sala.html', {'sucursales': sucursales})

def ver_sala(request):
    salas = Sala.objects.select_related('sucursal').all()
    return render(request, 'sala/ver_sala.html', {'salas': salas})

def actualizar_sala(request, id_sala):
    sala = get_object_or_404(Sala, pk=id_sala)
    sucursales = Sucursal.objects.all()
    return render(request, 'sala/actualizar_salas.html', {'sala': sala, 'sucursales': sucursales})

def realizar_actualizacion_sala(request, id_sala):
    sala = get_object_or_404(Sala, pk=id_sala)
    if request.method == 'POST':
        sala.numero_sala = int(request.POST.get('numero_sala') or sala.numero_sala)
        sala.tipo_sala = request.POST.get('tipo_sala') or sala.tipo_sala
        sala.capacidad = int(request.POST.get('capacidad') or sala.capacidad)
        sala.estado = request.POST.get('estado') or sala.estado
        sala.fecha_ultimo_mantenimiento = request.POST.get('fecha_ultimo_mantenimiento') or sala.fecha_ultimo_mantenimiento
        sala.asientos_especiales = int(request.POST.get('asientos_especiales') or sala.asientos_especiales)
        sucursal_id = request.POST.get('sucursal_id') or sala.sucursal_id
        sala.sucursal = get_object_or_404(Sucursal, pk=sucursal_id)
        sala.save()
        return redirect('ver_sala')
    return redirect('actualizar_sala', id_sala=id_sala)

def borrar_sala(request, id_sala):
    sala = get_object_or_404(Sala, pk=id_sala)
    if request.method == 'POST':
        sala.delete()
        return redirect('ver_sala')
    return render(request, 'sala/borrar_sala.html', {'sala': sala})