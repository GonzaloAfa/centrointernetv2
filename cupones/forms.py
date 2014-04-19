#encoding:utf-8
from django.forms import ModelForm
from django import forms

from cupones.models import Proceso


class NuevoProceso (ModelForm):
	class Meta:
		model = Proceso
