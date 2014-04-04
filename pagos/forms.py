#encoding:utf-8
from django.forms import ModelForm
from django import forms

from pagos.models import Historico


class NuevoPago(ModelForm):
	class Meta:
		model 	= Historico
		exclude	= ('descripcion',)
#Falta agregar 'tipo_historico'. pero necesito que funcione el choises de tipo_historico