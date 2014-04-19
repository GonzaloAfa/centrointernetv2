from django.db import models
from clientes.models import Cliente
# Create your models here.

PAGO = 1
COBRO = 2
DESCUENTO = 3

TIPO_HISTORICO = (	
		('Pago', 'Pago'),
		('Cobro', 'Cobro'),
		('Descuento', 'Descuento'),
		)

METODO_PAGO = (
	('Servipag', 'Servipag'),
	('Transferencia', 'Transferencia'),
	('Sucursal', 'Sucursal'),
	)



class MetodoPago(models.Model):
	metodo_pago 	= models.CharField(max_length=20, choices=METODO_PAGO)

	def __unicode__(self):
		return self.metodo_pago

class TipoHistorico(models.Model):
	tipo_historico	= models.CharField(max_length=20, choices=TIPO_HISTORICO)

	def __unicode__(self):
		return self.tipo_historico



class Historico(models.Model):
	cliente 		= models.ForeignKey(Cliente)
	datetime 		= models.DateTimeField(auto_now=True)
	cantidad 		= models.IntegerField()
	descripcion		= models.CharField(max_length=30, blank=True)
	metodo_pago 	= models.ForeignKey(MetodoPago)
	tipo_historico	= models.ForeignKey(TipoHistorico)

