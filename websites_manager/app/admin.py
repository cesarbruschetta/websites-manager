from django.contrib import admin

from models import Host, Evento, Comando, PainelControle, Script


admin.site.register(Host)
admin.site.register(Evento)
admin.site.register(Comando)
admin.site.register(Script)
admin.site.register(PainelControle)
