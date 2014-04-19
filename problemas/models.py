from django.db import models

from clientes.models import Cliente


ESTADO_PROBLEMA = (
	('Informado','Informado'),
	('Reparando','Reparando'),
	('Solucionado','Solucionado'),
	)


# Create your models here.
class TipoProblema(models.Model):
	tipo_problema	= models.CharField(max_length=20)
	def __unicode__(self):
		return self.tipo_problema

class EstadoProblema(models.Model):
	estado_problema	= models.CharField(max_length=20, choices=ESTADO_PROBLEMA)

	def __unicode__(self):
		return self.estado_problema

class Problema (models.Model):
	cliente 		= models.ForeignKey(Cliente)
	tipo_problema 	= models.ForeignKey(TipoProblema)
	comentario 		= models.TextField(blank=False)
	datetime 		= models.DateTimeField(auto_now=True)
	status 			= models.ForeignKey(EstadoProblema)
	descuento		= models.IntegerField()
