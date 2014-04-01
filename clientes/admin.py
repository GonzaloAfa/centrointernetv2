from django.contrib import admin

from clientes.models import Servicio, ClienteStatus, Red, Cliente


admin.site.register(Servicio)
admin.site.register(ClienteStatus)
admin.site.register(Red)
admin.site.register(Cliente)
