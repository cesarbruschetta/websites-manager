# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

class Host(models.Model):
    
    def __unicode__(self):
        host_name = '%s: %s' % (self.name,self.host_address)
        return unicode(host_name)
    
    name = models.CharField('Nome do Host', max_length=200)
    description = models.TextField('Descrição')
    
    host_address = models.CharField("Endereço do Host", max_length=200)
    ssh_port = models.IntegerField("Porta para Acesso SSH", default=22)
    username = models.CharField("Usuário de conexão", max_length=200)
    password = models.CharField("Senha do usuário", max_length=200)

    
class PainelControle(models.Model):
    
    def __unicode__(self):
        return self.name

    name = models.CharField('Nome do Painel', max_length=200)
    description = models.TextField('Descrição')        

    address = models.CharField("Endereço do painel de controle", max_length=200)

    
class Comando(models.Model):
    
    def __unicode__(self):
        return self.name
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    
    comando = models.CharField(max_length=200)
    is_action = models.BooleanField(default=True)

     
class Evento(models.Model):
    
    def __unicode__(self):
        return self.name
    
    name = models.CharField('Nome do eventos', max_length=200)
    description = models.TextField('Descrição')
    
    comando = models.ForeignKey(Comando)
    #if_true = models.ManyToManyField(Comando) #,'Ação se comando for verdadeiro')
    #if_false = models.ManyToManyField(Comando) #,'Ação se comando for falso')
    intervalo_tempo = models.CharField('Intervalo do eventos, em minutos', max_length=20)
    
    #Host para executar o evento
    host = models.ForeignKey(Host)
    
class Log(models.Model):

    host = models.ForeignKey(Host)
    date_creation = models.DateTimeField(default=datetime.now())
    error_log = models.TextField()
    
