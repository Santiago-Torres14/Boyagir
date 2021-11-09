from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Medicion
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async

class MeasurementDataConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        await self.accept()

        allData = await database_sync_to_async(Medicion.objects.all, thread_sensitive=True)()

        # TODO // Serialize the data obtained from allData
        serializedData = [json.dumps({'codBoya': data.codBoya, 'Medicion': data.Medicion, 'Fecha': data.Fecha}) for data in allData]

        # Send the information back to the client
        await self.send(serializedData)


    async def disconnect(self, close_code):
        pass