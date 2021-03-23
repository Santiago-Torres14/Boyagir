from rest_framework import routers
from .apiBoya import *
router=routers.DefaultRouter()
router.register("api/boya",BoyaViewSet,"boya")
router.register("api/sensor",SensorViewSet,"sensor")
router.register("api/afluente",AfluenteViewSet,"afluente")
router.register("api/medicion",MedicionViewSet,"medicion")
router.register("api/evento",EventoViewSet,"evento")
router.register("api/alerta",AlertaViewSet,"alerta")
urlpatterns=router.urls