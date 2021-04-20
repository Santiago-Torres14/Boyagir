from django.db import models

# Create your models here.
#from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Practica(models.Model):
    name=models.CharField(max_length=30)
    surname=models.CharField(max_length=40)
    birthyear=models.DateTimeField()
    birthplace=models.CharField(max_length=20)
class Departamento(models.Model):
    nombre = models.CharField(max_length=200, unique=True)

class Municipios(models.Model):
    nombre = models.CharField(max_length=200)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='municipios')
class Dano(models.Model):
    pass
class Afluente (models.Model):
    nombre=models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Afluente'
        verbose_name_plural = 'Afluentes'
class Sensor  (models.Model): 
    Tipo_Sensor= models.CharField(max_length=10) 
    Voltaje=models.IntegerField()
    Referencia= models.TextField()
class Circutio  (models.Model): 
    codSensor=models.ForeignKey(Sensor, null=True, blank=True, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Sensor'
        verbose_name_plural = 'Sensores'
class Mantenimiento(models.Model):
    nombre=models.CharField(max_length=50)
    Fecha=models.DateTimeField()
    costo=models.DecimalField(max_digits=5, decimal_places=2)
    codDano=models.ForeignKey(Circutio, null=False, blank=False, on_delete=models.CASCADE)    
class DetalleMantenimiento(models.Model):
    codMantenimeinto=models.ForeignKey(Departamento, null=False, blank=False, on_delete=models.CASCADE)
    codCircuito=models.ForeignKey(Circutio, null=False, blank=False, on_delete=models.CASCADE)    

class Boya (models.Model): 
    Nombre_Boya= models.CharField(max_length=50) 
    codDepert=models.ForeignKey(Departamento, null=False, blank=False, on_delete=models.CASCADE)
    codMuicipio= models.ForeignKey(Municipios, null=False, blank=False, on_delete=models.CASCADE)
    codRio=models.ForeignKey(Afluente, null=False, blank=False, on_delete=models.CASCADE)
    Latitud =models.CharField(max_length=50) 
    Longitud =models.CharField(max_length=50) 
    codCircuito = models.ForeignKey(Circutio, null=False, blank=False, on_delete=models.CASCADE)
    Fecha=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Boya'
        verbose_name_plural = 'Boyas'
 


class Medicion (models.Model):
    codBoya = models.ForeignKey(Boya, null=True, blank=True, on_delete=models.CASCADE)
    Medicion = JSONField()
    #Medicion=models.CharField(max_length=100)
    Fecha=models.DateTimeField(auto_now_add=True)
class TipoAlertas(models.Model):
    Nombre=models.CharField(max_length=30)
    nivel=models.IntegerField()

class Alerta (models.Model):
    codBoya = models.ForeignKey(Boya, null=True, blank=True, on_delete=models.CASCADE)
    Nivel=models.CharField(max_length=100)
    Descripcion=models.TextField()

    class Meta:
        verbose_name = 'Alerta'
        verbose_name_plural = 'Alertas'





