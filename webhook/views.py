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


import bs4
import requests

'''
def scrap_image(key):
    res = requests.get('https://duckduckgo.com/' + key + '?iax=1&ia=images&iaf=size%3Al')
    r = bs4.BeautifulSoup(res.text)
    import itertools

    def trios(seq):
         is1 = itertools.islice(iter(seq), 0, None, 3)
         is2 = itertools.islice(iter(seq), 1, None, 3)
         return itertools.izip(is1, is2)

    s = [r.select('.data_wide_table tr td')[td].getText() for td in range(len(r.select('.data_wide_table tr td')))]
    for x, y in trios(s):
        print x,y

'''
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
                        joke_text = "Hello, Hope you are doing great! Type a name of an agricultural commodity to know its price in Kenya eg 'Carrots'."
                    elif 'Hi' in message["message"]["text"].encode("utf-8"):
                        joke_text = "Hi, Hope you are doing great! Type a name of an agricultural commodity to know its price in Kenya eg 'Carrots'."
                    else:
                        jsondata = requests.get("http://opendata.arcgis.com/datasets/3e3c700709b14efa9a5c11619bf5539d_0/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json").json()['features']
                        joke_text = ""
                        for n in jsondata:
                            if message["message"]["text"].encode("utf-8") in n["attributes"]["Commodity_Type"].encode("utf-8"):
                                joke_text = ("Produce Variety : " + n["attributes"]["Produce_Variety"] + "\n " +
                                             "Commodity Type : " + n["attributes"]["Commodity_Type"] + "\n " +
                                             "Unit : " + n["attributes"]["Unit"] + "\n " +
                                             "Volume in Kgs : " + str(n["attributes"]["Volume_in_Kgs"]) + "\n " +
                                             "Values in Ksh : " + n["attributes"]["Values_in_Ksh"])
                                #joke_text += joke_text

                    if joke_text:
                        pass
                    else:
                        joke_text = "Not Found"
                    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%'EAABqdFKpfcoBAIVS1oAWcZCiyalYN7aN5uLcdZA2V2xnawa8BD0GlI0LI7Sv9ZBuzZBvvZALF3QjpGUgjdEVbzyAZCDuezFFZAk1qs42PoxBTrXkgfJpKFWJrnpcecmPy6Ej4ZBvVjKdTM71LIhwgIOfSWtgk1zLPblyZA1lGFqjH91xNyZADndpU6ZB3sPzMWvVZAoZD'
                    response_msg = json.dumps({"recipient":{"id":message['sender']['id']}, "message":{"text":joke_text}})
                    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
                    pprint(status.json())
        return HttpResponse()
