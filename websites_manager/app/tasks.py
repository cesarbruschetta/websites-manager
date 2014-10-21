# -*- coding: utf-8 -*-
from celery.task import task
from celery.contrib import rdb



from websites_manager.app.models import *

@task()
def taskMagagerGlobalTasks(type=1,id_model=2,**kwargs):
    x = 1+2 
    
    rdb.set_trace()  # <- set breakpoint
    
    print 'testetetststst'
    
    return x
    