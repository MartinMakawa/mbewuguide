import os
import django
from django.core.asgi import get_asgi_application
django.setup()  
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import community.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mbewuguide_backend.settings')


application = ProtocolTypeRouter({
    "http": django.core.asgi.get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            community.routing.websocket_urlpatterns
        )
    ),
})
