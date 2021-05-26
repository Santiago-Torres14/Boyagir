import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE','boyagir.settings')
app=Celery('boyagir')
app.config_from_object('django.conf:settings',namespace='CELERY')
app.conf.beat_schedule={
    'get_joke_3s':{
        'task':'graphrealtime.tasks.get_medicion',
        'schedule':10.0

    }

}
app.autodiscover_tasks()
