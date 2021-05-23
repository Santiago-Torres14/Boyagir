from .models import *
from rest_framework import serializers

class History(serializers.ModelSerializer):
    def __init__(self, model, *args, fields='__all__', **kwargs):
        self.Meta.model = model
        self.Meta.fields = fields
        super().__init__()

    class Meta:
        pass

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
        history = serializers.SerializerMethodField()
    def get_history(self, obj):
            model = obj.history.__dict__['model']
            fields = ['history_id', ]
            lll
            serializer = sHistory(model, obj.history.all().order_by('history_date'), fields=fields, many=True)
            serializer.is_valid()
            return serializer.data
        
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
    

class  CircuitoSerializer( serializers.ModelSerializer):
    class Meta:
        model=Circutio
        fields="__all__"
class  ArtistaSerializer( serializers.ModelSerializer):
    class Meta:
        model=Artista
        fields="__all__"


        
class BoyaTSerializer(serializers.ModelSerializer):

   
   
    afluente = AfluenteSerializer(many=True)
    

    class Meta:
        model = Afluente
        fields = (
            'codAfluente',
            'nombreAfluente',
            )



