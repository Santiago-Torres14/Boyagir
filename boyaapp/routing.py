from django.urls import path
from .consumers import MeasurementDataConsumer

ws_urlpatterns=[
    path('ws/measurement-data/', MeasurementDataConsumer.as_asgi())
]