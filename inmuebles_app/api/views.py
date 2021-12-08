import re
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from  inmuebles_app.models import Inmueble
from inmuebles_app.api.serializers import InmuebleSerializer
#from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

class InmuebleListAV(APIView):
    
    def get(self, request):
        inmuebles = Inmueble.objects.all()
        serializer = InmuebleSerializer(inmuebles, many=True)
        print("This is a GET Method and the data serializated is:",serializer.data)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = InmuebleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("This is a POST Method, the serialization is valid and the data serializated is:",serializer.data)
            return Response(serializer.data)
        else:
            print(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
 
class InmuebleDetalleAV(APIView):
     
    def get(self, request, pk):
        try:
            inmueble = Inmueble.objects.get(pk=pk)
            print(inmueble)
        except Inmueble.DoesNotExist:
            return Response({'Error': 'Inmueble no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = InmuebleSerializer(inmueble)
        print(serializer.data)
        return Response(serializer.data)
     
    def put(sef, request, pk):
        try:
            inmueble = Inmueble.objects.get(pk=pk)
        except Inmueble.DoesNotExist:
            return Response({'Error': 'Inmueble no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = InmuebleSerializer(inmueble, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      
    
    def delete(sef, request, pk):
        try:
            inmueble = Inmueble.objects.get(pk=pk)
        except Inmueble.DoesNotExist:
            return Response({'Error': 'Inmueble no encontrado'}, status=status.HTTP_404_NOT_FOUND)   
        inmueble.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)           
                    
            




#Comentar todo con ctrl + k + c
# @api_view(['GET','POST'])     #podria ser tambien @api_view(), ya que por default es un metodo GET
# def inmueble_list(request):
#     if request.method == 'GET':
#         inmuebles = Inmueble.objects.all()
#         serializer = InmuebleSerializer(inmuebles, many=True)  #many , se usa para indicar que seran muchos datos
#         print("This was a GET request", serializer)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         data_deserializer= InmuebleSerializer(data=request.data)
#         if data_deserializer.is_valid():
#             data_deserializer.save()
#             print(data_deserializer)
#             return Response(data_deserializer.data)
#         else:
#             return Response(data_deserializer.errors)
        


# @api_view(['GET', 'PUT', 'DELETE'])      #podria ser tambien @api_view(), ya que por default es un metodo GET
# def inmueble_detalle(request, pk):
#     if request.method == 'GET':
#         try:    
#             inmueble = Inmueble.objects.get(pk=pk)  # pk = primary Key, aqui solo estamos regresando un solo dato
#             serializer = InmuebleSerializer(inmueble)
#             return Response(serializer.data)
#         except Inmueble.DoesNotExist:
#             return Response({'Error': 'El inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'PUT':
#         inmueble = Inmueble.objects.get(pk=pk)
#         data_deserializer = InmuebleSerializer(inmueble, data=request.data)  
#         if data_deserializer.is_valid():
#             data_deserializer.save()
#             return  Response(data_deserializer.data)
#         else:
#             return Response(data_deserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'DELETE':
#         try:
#             inmueble = Inmueble.objects.get(pk=pk)
#             inmueble.delete()
#         except Inmueble.DoesNotExist:
#             return Response({'Error': 'El objecto ID no existe'}, status=status.HTTP_404_NOT_FOUND)
        
#         return Response(status=status.HTTP_204_NO_CONTENT)
            

     