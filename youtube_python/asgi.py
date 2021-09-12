# mysite/asgi.py
import os

import django
from channels.auth import AuthMiddlewareStack
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path

import youtube
from youtube.room import ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youtube.settings')
django.setup()


websocket_urlpatterns = [
	re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
	"http": AsgiHandler(),
	"websocket": AuthMiddlewareStack(
		URLRouter(
			websocket_urlpatterns
		)
	),
	# Just HTTP for now. (We can add other protocols later.)
})
