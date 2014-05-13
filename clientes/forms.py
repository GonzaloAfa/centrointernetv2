#encoding:utf-8
from django.forms import ModelForm
from django import forms

from clientes.models import Cliente


class NuevoCliente(ModelForm):
	class Meta:
		model = Cliente
		exclude = ('status',)

class EditarCliente(ModelForm):
	class Meta:
		model 	= Cliente
		exclude	= ('username',)
