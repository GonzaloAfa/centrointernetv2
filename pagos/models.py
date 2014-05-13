from django.db import models
from clientes.models import Cliente
# Create your models here.

PAGO = 'Pago'
COBRO = 'Cobro'
DESCUENTO = 'Descuento'

TIPO_HISTORICO = (	
		(PAGO, 'Pago'),
		(COBRO, 'Cobro'),
		(DESCUENTO, 'Descuento'),
		)

METODO_PAGO = (
	('Servipag', 'Servipag'),
	('Transferencia', 'Transferencia'),
	('Sucursal', 'Sucursal'),
	)


class Historico(models.Model):
	cliente 		= models.ForeignKey(Cliente)
	datetime 		= models.DateTimeField(auto_now=True)
	cantidad 		= models.IntegerField()
	descripcion		= models.CharField(max_length=30, blank=True)
	metodo_pago 	=  models.CharField(max_length=20, choices=METODO_PAGO)
	tipo_historico	= models.CharField(max_length=20, choices=TIPO_HISTORICO)

