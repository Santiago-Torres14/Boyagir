from .models import *
from rest_framework import serializers

class  BoyaSerializer( serializers.ModelSerializer):
    class Meta:
        model=Boya
        fields="__all__"
class  SensorSerializer( serializers.ModelSerializer):
    class Meta:
        model=Sensor
        fields="__all__"
class  AfluenteSerializer( serializers.ModelSerializer):
    class Meta:
        model=Afluente
        fields="__all__"
class  MedicionSerializer( serializers.ModelSerializer):
    class Meta:
        model=Medicion
        fields="__all__"
class  AlertaSerializer( serializers.ModelSerializer):
    class Meta:
        model=Alerta
        fields="__all__"
class MunicipiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipios
        fields = ("id","nombre")
class DepartamentoSerializer(serializers.ModelSerializer):
    municipios = MunicipiosSerializer(many=True)
    class Meta:
        model = Departamento
        fields = ("id","nombre","municipios")
    def create(self, validated_data):
	    departamento = Departamento( nombre=validated_data.get("nombre") )
	    departamento.save()        
	    municipios = validated_data.get('municipios')
	    for municipio in municipios:
	      Municipios.objects.create(departamento=departamento, **municipio)
        
	    return validated_data

class MunicipiosSolasSerializer(serializers.ModelSerializer):
    departamento_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Municipios
        fields = ("nombre","departamento","departamento_id")
        depth = 1
class PracticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practica
        fields = "__all__"
    

class  CircuitoSerializer( serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Circutio
        fields="__all__"

        




