from .serializers import *
from .models import *
from rest_framework import viewsets,permissions
from rest_framework.filters import SearchFilter
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def  foraneasBoya(request):
    municipios=Municipios.objects.all()
    afluente=Afluente.objects.all()
    BoyaMuni=MunicipiosSerializer(municipios,many=True)
    BoyaAfluente=AfluenteSerializer(afluente,many=True)
    resultadoBoya=BoyaMuni.data+BoyaAfluente.data
    return Response(resultado)

class BoyaViewSet(viewsets.ModelViewSet):
    queryset=Boya.objects.all()
    permision_classes=[permissions.AllowAny]
    serializer_class=BoyaSerializer
class PracticaViewSet(viewsets.ModelViewSet):
    queryset=Practica.objects.all()
    permision_classes=[permissions.AllowAny]
    serializer_class=PracticaSerializer
class SensorViewSet(viewsets.ModelViewSet):
    queryset=Sensor.objects.all()
    permision_classes=[permissions.AllowAny]
    serializer_class=SensorSerializer
class AfluenteViewSet(viewsets.ModelViewSet):
    queryset=Afluente.objects.all()
    permision_classes=[permissions.AllowAny]
    serializer_class=AfluenteSerializer
class MedicionViewSet(viewsets.ModelViewSet):
    queryset=Medicion.objects.all()
    permision_classes=[permissions.AllowAny]
    serializer_class=MedicionSerializer
class MedicionViewSet(viewsets.ModelViewSet):
    queryset=Medicion.objects.all()
    permision_classes=[permissions.AllowAny]
    serializer_class=MedicionSerializer
class BoyaViewSet(viewsets.ModelViewSet):
    queryset=Boya.objects.all()
    permision_classes=[permissions.AllowAny]
    serializer_class=BoyaSerializer
class AlertaViewSet(viewsets.ModelViewSet):
    queryset=Alerta.objects.all()
    permision_classes=[permissions.AllowAny]
    serializer_class=AlertaSerializer
class DepartamentoViewSet(viewsets.ModelViewSet):
    model = Departamento
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
class MunicipioViewSet(viewsets.ModelViewSet):
    model = Municipios
    queryset = Municipios.objects.all()
    serializer_class = MunicipiosSolasSerializer
class CircuitoViewSet(viewsets.ModelViewSet):
    queryset=Circutio.objects.all()
    permision_classes=[permissions.AllowAny]
    serializer_class=CircuitoSerializer
class ArtistaViewSet(viewsets.ModelViewSet):
    queryset=Artista.objects.all()
    permision_classes=[permissions.AllowAny]
    
    serializer_class=ArtistaSerializer
class AfluentesViewSet(viewsets.ModelViewSet):
    permision_classes=[permissions.AllowAny]
    serializer_class=BoyaTSerializer







