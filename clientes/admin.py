from django.contrib import admin

from clientes.models import Servicio, Red, Cliente


admin.site.register(Servicio)
admin.site.register(Red)
admin.site.register(Cliente)
