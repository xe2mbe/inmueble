from django.http.response import JsonResponse
from django.shortcuts import render

from inmuebles_app.models import Inmueble

# Create your views here.
""" 

def inmueble_list(request):
    inmuebles = Inmueble.objects.all()
    data = {
        'inmuebles' : list(inmuebles.values())
        
    }
    #print(data)
    return JsonResponse(data)

def inmueble_detalle(request, pk):     #pk = primary key
    inmueble = Inmueble.objects.get(pk=pk)
    data = {
        'direccion' : inmueble.direccion,
        'pais' : inmueble.pais,
        #'imagen' : inmueble.imagen,
        'activo' : inmueble.active,
        'descripcion' : inmueble.descripcion,                  
    }
    #print(data)
    return JsonResponse(data) """