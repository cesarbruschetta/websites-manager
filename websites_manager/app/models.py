# -*- coding: utf-8 -*-
from django.db import models

class Host(models.Model):
    
    def __unicode__(self):
        host_name = '%s: %s' % (self.company.name,self.host_address)
        return unicode(host_name)
    
    host_address = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    
    ssh_port = models.IntegerField(default=22)
    
    path = models.CharField(max_length=200,default='/opt/instances')
    python_path = models.CharField(max_length=200,default='/opt/python')
    
