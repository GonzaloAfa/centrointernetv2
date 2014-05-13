#encoding:utf-8
from django.forms import ModelForm
from django import forms

from clientes.models import Cliente
from clientes.utils import validar_rut, limpiar_rut


class NuevoCliente(ModelForm):
	class Meta:
		model = Cliente
		exclude = ('status',)

	def clean(self):
		rut = limpiar_rut(self.cleaned_data['rut'])
		if validar_rut(rut):
			self.cleaned_data['rut'] = rut
			return self.cleaned_data
		raise forms.ValidationError(
			                "Rut no es valido"
			            )
		
		



class EditarCliente(ModelForm):
	class Meta:
		model 	= Cliente
		exclude	= ('username',)

	def clean(self):
		rut = limpiar_rut(self.cleaned_data['rut'])
		if validar_rut(rut):
			self.cleaned_data['rut'] = rut
			return self.cleaned_data
		raise forms.ValidationError(
			                "Rut no es valido"
			            )

