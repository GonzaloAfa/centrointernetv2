#encoding:utf-8
from django.forms import ModelForm
from django import forms

from pagos.models import Historico


class NuevoPago(ModelForm):
	class Meta:
		model 	= Historico
		exclude	= ('descripcion',)

#	tipo_historico = forms.CharField(widget=forms.HiddenInput)
