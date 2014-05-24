from django.db import models

from clientes.models import Cliente


ESTADO_PROBLEMA = (
	('Informado','Informado'),
	('Reparando','Reparando'),
	('Solucionado','Solucionado'),
	)

TIPO_PROBLEMA = (
	('No funciona Internet','No funciona Internet'),
	('DNS','DNS'),
	('Mucho lag','Mucho Lag'),
	('Internet cortado','Internet Cortado'),
	)


class Problema (models.Model):
	cliente 		= models.ForeignKey(Cliente)
	tipo_problema 	= models.CharField(max_length=20, choices=TIPO_PROBLEMA)
	comentario 		= models.TextField(blank=False)
	datetime 		= models.DateTimeField(auto_now=True)
	status 			= models.CharField(max_length=20, choices=ESTADO_PROBLEMA)