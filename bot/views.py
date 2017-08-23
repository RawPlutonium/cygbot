# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
import json
import pprint

# Create your views here.
PAT = "EAALvgVZA7qVcBAEBZBOPROoZAhVJANIFOik1OJJ8nXgeBD2OVvtM0tDKgphu4n6VUFLPZAUHovjOgnFu5uPO8wLRZCg2g2P6ZByrm10XKy2eZCIO3rrzFv7OMQAIAl37rIqOu8hWlfjDzro8RQADWlE6goFXXrE45ZBm6xbw4ZCqECAZDZD"

class cygbotview(generic.View):
    def bview(self, request, *args, **kwargs):
         if self.request.GET['hub.verify_token'] == '90293269':
            return HttpResponse(self.request.GET['hub.challenge'])
         else :
            return HttpResponse('Invalid Token !')
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)
    #Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):
        #Converts the text payload into a python dict
        in_mesg = json.loads(self.request.body.decode('utf-8'))
        #going through every entry since they might send
        for entry in in_mesg['entry']:
            for message in entry['messaging']:
                #check to make sure the received call is a message call
                #This might be delivery , optin, postback for other events
                if 'message' in message:
                    #Print the message to the terminal
                    pprint(message)
                    post_msg_to_facebook(message['sender']['id'], message['message']['text'])
        return HttpResponse
def post_msg_to_facebook(fbid, received_message):
    post_msg_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=<PAT>'
    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":received_message}})
    status = requests.post(post_msg_url, headers={"Content-Type": "application/json"},data=response_msg)
    pprint(status.json())
