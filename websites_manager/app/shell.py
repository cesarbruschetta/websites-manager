# -*- coding: utf-8 -*-

from random import choice

from fabric.api import *
from fabric.context_managers import *



class FabricSupport(object):

    def setupConnection(self,host):
        env.raise_error_on_prompts = True
        env.host_string = "%s@%s:%s" % (host.username,
                                        host.host_address,
                                        host.ssh_port)
        env.password = host.password
        
    def testConnection(self,host):
        
        env.raise_error_on_prompts = True
        env.host_string = "%s@%s:%s" % (host.username,
                                        host.host_address,
                                        host.ssh_port)
        env.password = host.password
        try:
            #Testando connection
            with settings(hide('warnings', 'running', 'stdout', 'stderr'),
                          warn_only=True):
                cd('/tmp')
            #Testano privilegio de root
            num = []
            for i in range(25):
                num.append(str(choice(range(10))))
            num = ''.join(num)
            
            try:
                sudo('mkdir /root/.testing_connection-%s' % num)
                sudo('rm -rf /root/.testing_connection-%s' % num)
            except:
                #self.sendMessage(u'The user has no root privileges' % instance.host.host_address)
                return u'The user has no root privileges' % host.host_address
        except:
            #self.sendMessage(u'Unable to connect to host %s' % instance.host.host_address)
            return u'Unable to connect to host %s' % host.host_address
        
        return None      