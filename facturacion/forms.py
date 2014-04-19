#encoding:utf-8
from bootstrap3_datetime.widgets import DateTimePicker
from django.forms import ModelForm

from django import forms

from facturacion.models import Proceso


class NuevoProceso (ModelForm):
	class Meta:
		model = Proceso

	periodo_inicio = forms.DateField( widget=DateTimePicker(
		options={"format": "YYYY-MM-DD", "pickSeconds": False}))	