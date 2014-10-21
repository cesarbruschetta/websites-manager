from django.contrib import admin

from models import Host, Comando, PainelControle, Script

admin.site.register(PainelControle)
admin.site.register(Host)

admin.site.register(Comando, admin_class=Comando.Admin)
admin.site.register(Script)

