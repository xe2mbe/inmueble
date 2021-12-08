import re
from django.db.models import fields
from rest_framework import serializers

from inmuebles_app.models import Inmueble

class InmuebleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inmueble
        fields = "__al__"  #Serializa todos los datos del modelo
        
        #fields = ['id', 'pais', 'active'] # De esta forma se serializan los campos que queremos enviar
        
        #fields = "__al__"  # Para excluir campos, podemos seleccionar todos y despues excluimos con:
        #exclude = ['id']  # en este caso estamos excluyendo de todos los campos el 'id' de la serializacion
        
        
        
        


# class InmuebleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     direccion = serializers.CharField()
#     pais = serializers.CharField()
#     descripcion = serializers.CharField()
#     imagen = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validate_data):   #def create() es una funcion propia de serializers.
#         return Inmueble.objects.create(**validate_data)
    
#     def update(self, instance, validate_data):    #def update() es una funcion propia de serializers.
#         instance.direccion = validate_data.get('direccion', instance.direccion)
#         instance.pais = validate_data.get('pais', instance.pais)
#         instance.descripcion = validate_data.get('descripcion', instance.descripcion)
#         instance.imagen = validate_data.get('imagen', instance.imagen)
#         instance.active = validate_data.get('active', instance.active)
#         instance.save()
#         return instance