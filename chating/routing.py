from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer.as_asgi()),
]

#re_path -> 내부 라우터가 미들웨어에 감싸져 있ㅇ을 경우 path()가 제대로 작동하지 않을 수 있기에 사전에 방지하고자 사용합니다