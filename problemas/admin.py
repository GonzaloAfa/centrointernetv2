from django.contrib import admin

from problemas.models import TipoProblema, Problema
# Register your models here.

admin.site.register(TipoProblema)
admin.site.register(Problema)