# -*- coding: utf-8 -*-

from django import template
from django.contrib.sites.models import Site


register = template.Library()
    
@register.filter
def soma(x,y):
    return x+str(y)

