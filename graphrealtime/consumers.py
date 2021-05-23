import json
from random import randint
from asyncio import sleep
from channels.generic.websocket import AsyncWebsocketConsumer


class GraphConsumer(AsyncWebsocketConsumer):
   async def connect(self):
       await self.channel_layer.group_add('Medicion',self.channel_name)
       await self.accept()
   async def disconnect(self):
        await self.channel_layer.group_discard('Medicion',self.channel_name)
   async def send_medicion(self,event):
       text_message=event['text']
       await self.send(text_message)

      
