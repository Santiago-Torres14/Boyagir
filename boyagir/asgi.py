"""
ASGI config for boyagir project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth    import AuthMiddlewareStack
from graphrealtime.routing import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boyagir.settings')
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket':AuthMiddlewareStack(URLRouter(ws_urlpatterns))
    # Just HTTP for now. (We can add other protocols later.)
})
