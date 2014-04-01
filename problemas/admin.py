from django.contrib import admin

from problemas.models import TipoProblema, EstadoProblema, Problema
# Register your models here.

admin.site.register(TipoProblema)
admin.site.register(EstadoProblema)
admin.site.register(Problema)