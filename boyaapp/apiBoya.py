from .serializers import *
from .models import *
from rest_framework import viewsets,permissions

class BoyaViewSet(viewsets.ModelViewSet):
    queryset=Boya.objects.all()
    permision_classes=[permissions.AllowAny]
    serializer_class=BoyaSerializer

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


class EventoViewSet(viewsets.ModelViewSet):
    queryset=Evento.objects.all()
    permision_classes=[permissions.AllowAny]
    serializer_class=EventoSerializer


class AlertaViewSet(viewsets.ModelViewSet):
    queryset=Alerta.objects.all()
    permision_classes=[permissions.AllowAny]
    serializer_class=AlertaSerializer
