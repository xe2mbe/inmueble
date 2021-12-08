from django.urls import path
#from inmuebles_app.api.views import inmueble_list, inmueble_detalle
from inmuebles_app.api.views import InmuebleListAV, InmuebleDetalleAV


urlpatterns = [
    path('list/', InmuebleListAV.as_view(), name='inmueble-list'), 
    path('<int:pk>', InmuebleDetalleAV.as_view(), name='inmueble-detalle'),  
]
