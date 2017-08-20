# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http.response import HttpResponse
# Create your views here.
PAT = "EAALvgVZA7qVcBAEBZBOPROoZAhVJANIFOik1OJJ8nXgeBD2OVvtM0tDKgphu4n6VUFLPZAUHovjOgnFu5uPO8wLRZCg2g2P6ZByrm10XKy2eZCIO3rrzFv7OMQAIAl37rIqOu8hWlfjDzro8RQADWlE6goFXXrE45ZBm6xbw4ZCqECAZDZD"
def bview(request):
    return HttpResponse("Hello World!")
