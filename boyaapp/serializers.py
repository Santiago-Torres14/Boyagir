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
class  EventoSerializer( serializers.ModelSerializer):
    class Meta:
        model=Evento
        fields="__all__"
class  AlertaSerializer( serializers.ModelSerializer):
    class Meta:
        model=Alerta
        fields="__all__"





