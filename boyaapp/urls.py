from rest_framework import routers
from .apiBoya import *
from .views import MedicionGet
router=routers.DefaultRouter()

router.register("api/boya",BoyaViewSet,"boya")
router.register("api/sensor",SensorViewSet,"sensor")
router.register("api/afluente",AfluenteViewSet,"afluente")
router.register("api/medicion",MedicionViewSet,"medicion")
router.register("api/alerta",AlertaViewSet,"alerta")
router.register("api/departamento",DepartamentoViewSet,"departamento")
router.register("api/municipio",MunicipioViewSet,"municipio")
router.register("api/circuito",CircuitoViewSet,"circuito")





urlpatterns=router.urls