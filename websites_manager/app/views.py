# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from shell import FabricSupport

from models import Host, PainelControle

login_url = '/login'

def hello(request):
    return HttpResponse("Hello, world. You're at the poll index.")


@login_required(login_url=login_url)
def home(request):
    context = {}
    
    return render_to_response('home.html', context,
        context_instance=RequestContext(request))
    
@login_required(login_url=login_url)    
def paineis(request):
    context = {}

    context['itens'] = PainelControle.objects.all()
    
    return render_to_response('paineis.html', context,
        context_instance=RequestContext(request))

@login_required(login_url=login_url)    
def painel(request,id):
    context = {}
    
    context['itens'] = PainelControle.objects.all() 
    
    context['painel'] = PainelControle.objects.get(id=id)
    
    return render_to_response('painel.html', context,
        context_instance=RequestContext(request))
        