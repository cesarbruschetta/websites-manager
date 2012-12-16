# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext



def home(request):
    
    return HttpResponse("Hello, world. You're at the poll index.")