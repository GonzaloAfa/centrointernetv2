#encoding:utf-8
from django.forms import ModelForm
from django import forms

from centrointernet.models import NetworkConnection
from centrointernet.models import Service
from centrointernet.models import ClientStatus
from centrointernet.models import Client
from centrointernet.models import TypeProblem 
from centrointernet.models import Problem
from centrointernet.models import ProblemStatus
from centrointernet.models import Historical

class ContactForm(forms.Form):
	email 	= forms.EmailField(label='Email')
	message	= forms.CharField(widget=forms.Textarea, label='Mensaje')



class NewClient(ModelForm):
	class Meta:
		model = Client

class NewProblem(ModelForm):
	class Meta:
		model = Problem

class NewPay(ModelForm):
	class Meta:
		model = Historical


class UpdateClientForm(forms.Form):
	phone = forms.CharField(widget=forms.Textarea, label='Teléfono')
	email = forms.EmailField(label='Email')
