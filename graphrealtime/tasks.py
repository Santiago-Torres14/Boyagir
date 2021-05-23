import requests
from channel.layer import get_channel_layer
from asgiref.sync import async_to_sync
from celery import shared_task
channel_layer=get_channel_layer()
@shared_task
def get_medicion(requests):
    url="https://boyagir.herokuapp.com/api/medicion/"
    response=requests.get(url).json()

    size=len(response)
    for item in range(size-50,size):
        print(response[item]['Medicion'])
    x= response[size-1]["Medicion"]
    print(x)
    return 5+6
    #async_to_sync(channel_layer.group_send)('Medicion',{'type':'send_medicion','text':x})
    
    
    



   # return render(request,'base.html',context={"text":"Hello world"})
