"""
from channels.routing import route

channel_routing = [
    route('websocket.receive', 'webhook.consumers.messenger_consumer'),
]

"""
from channels import route
from .consumers import ws_connect, ws_receive, ws_disconnect, chat_join, chat_leave, chat_send

#from channels.staticfiles import StaticFilesConsumer


# There's no path matching on these routes; we just rely on the matching
# from the top-level routing. We could path match here if we wanted.
channel_routing = [
    
    #route('http.request', StaticFilesConsumer()),
    # Called when WebSockets connect
    route("websocket.connect", ws_connect),

    # Called when WebSockets get sent a data frame
    route("websocket.receive", ws_receive),

    # Called when WebSockets disconnect
    route("websocket.disconnect", ws_disconnect),
]

# You can have as many lists here as you like, and choose any name.
# Just refer to the individual names in the include() function.
custom_routing = [
    # Handling different chat commands (websocket.receive is decoded and put
    # onto this channel) - routed on the "command" attribute of the decoded
    # message.
    route("webhook.receive", chat_join, command="^join$"),
    route("webhook.receive", chat_leave, command="^leave$"),
    route("webhook.receive", chat_send, command="^send$"),
]
