# from channels.auth import AuthMiddlewareStack      # to identify the username (only authenticated user) it will allow us to utilize authentication
# from channels.routing import ProtocolTypeRouter, URLRouter
# import chat.routing


# # instead of using our urls we can use ProtocolTypeRouter (WS)
# application = ProtocolTypeRouter({
#     'websocket': AuthMiddlewareStack(
#         URLRouter(
#             chat.routing.websocket_urlpatterns
#         )
#     ),
# })

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from chat import consumers

# URLs that handle the WebSocket connection are placed here.
websocket_urlpatterns=[
                    re_path(
                        r"ws/chat/(?P<chat_box_name>\w+)/$", consumers.ChatRoomConsumer.as_asgi()
                    ),
                ]

application = ProtocolTypeRouter( 
    {
        "websocket": AuthMiddlewareStack(
            URLRouter(
               websocket_urlpatterns
            )
        ),
    }
)