# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


from django.views import generic
from django.http.response import HttpResponse
# Create your views here.

import json, requests, random, re
from pprint import pprint


from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class messenger(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == 'avenues3':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        # Converts the text payload into a python dictionary
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        # Facebook recommends going through every entry since they might send
        # multiple messages in a single call during high load
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                # Check to make sure the received call is a message call
                # This might be delivery, optin, postback for other events
                if 'message' in message:
                    if 'Hello' in message["message"]["text"].encode("utf-8"):
                        reply = "Hello, Hope you are doing great! Type a name of an agricultural commodity to know its price in Kenya eg 'Carrots'."
                    elif 'Hi' in message["message"]["text"].encode("utf-8"):
                        reply = "Hi, Hope you are doing great! Type a name of an agricultural commodity to know its price in Kenya eg 'Carrots'."
                    else:
                        reply = "Parrot:\n" + message["message"]["text"].encode("utf-8")

                    
                    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%'EAAULqvC7u8cBAMZBZAplMhGuPbYWjuCkDqxxeF2Vm7ozfL1uZClrhXvVxMh5JY1DlFK8jNlBbZAVtf8D2Qsry8cBQFNWZANgzaZB2z769rSIkXtkTCnJ83aK6JsBxLSulmC2OAOdQ3qJZCWnC2pjLiN5pnVHVZCZBSVbktU5HG3OARAZDZD'
                    response_msg = json.dumps({"recipient":{"id":message['sender']['id']}, "message":{"text":reply}})
                    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
                    pprint(status.json())
        return HttpResponse()







