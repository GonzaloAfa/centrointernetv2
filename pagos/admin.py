from django.contrib import admin

from pagos.models import TipoHistorico, MetodoPago, Historico

admin.site.register(TipoHistorico)
admin.site.register(MetodoPago)
admin.site.register(Historico)
