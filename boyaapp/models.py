from django.db import models

# Create your models here.
from django.contrib.postgres.fields import ArrayField
#from django.contrib.postgres.fields import JSONField

# Create your models here.
class Boya (models.Model): 
    Nombre_Boya= models.CharField(max_length=50) 
    Latitud =models.CharField(max_length=50) 
    Longitud =models.CharField(max_length=50)  
''''class Sensor  (models.Model): 
    Boya = models.ForeignKey(Boya, null=True, blank=True, on_delete=models.CASCADE)
    Tipo_Sensor= models.CharField(max_length=10) 
    Codigo_Sensor= models.IntegerField(10)
    Voltaje=models.IntegerField()
    Referencia= models.TextField(10)
class Afluente (models.Model):
    Boya = models.ForeignKey(Boya, null=True, blank=True, on_delete=models.CASCADE) 
    Codigo_Afluente= models.IntegerField(10)
    Nombre_Afluente=models.CharField(max_length=100)
    Nombre_de_departamento=models.CharField(max_length=100)
    Nombre_de_municipio=models.CharField(max_length=100)
class Medicion (models.Model):
    Boya = models.ForeignKey(Boya, null=True, blank=True, on_delete=models.CASCADE)
   # Medicion = JSONField()
    Medicion=models.CharField(max_length=100)
    Fecha=models.DateTimeField(auto_now_add=True)
class Evento (models.Model): 
    Medicion = models.ForeignKey(Medicion, null=True, blank=True, on_delete=models.CASCADE)
    Descripcion=models.TextField(200) 
class Alerta (models.Model):
    Evento = models.OneToOneField(Evento, null=True, blank=True, on_delete=models.CASCADE) 
    Nivel=models.CharField(max_length=100)
    Descripcion=models.TextField(200)
'''

