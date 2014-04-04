#encoding:utf-8
from django.forms import ModelForm
from django import forms

from problemas.models import Problema


class NuevoProblema(ModelForm):
	class Meta:
		model = Problema

class EditarProblema(ModelForm):
	class Meta:
		model 	= Problema
		exclude	= ('cliente', 'tipo_problema') 