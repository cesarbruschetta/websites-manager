# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#Views methods aplicação
from websites_manager.app.views import *

from settings import PATH_STATIC

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home, name='home'),
    
    url(r'^hello/$', hello, name='hello'),
    
    url(r'^painel/$', paineis, name='Paineis'),
    
    url(r'^painel/(?P<id>\w{0,50})$', painel, name='Painel'),
    # url(r'^websites_manager/', include('websites_manager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # Autenticação
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$','django.contrib.auth.views.logout_then_login',name='logout'),
    
    #Static
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.ico'}),
    
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': PATH_STATIC, 'show_indexes': False}),      
    
)
