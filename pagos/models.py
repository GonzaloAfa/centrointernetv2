from django.db import models
from clientes.models import Cliente
# Create your models here.

class MetodoPago(models.Model):
	metodo_pago 	= models.CharField(max_length=20)

	def __unicode__(self):
		return self.metodo_pago

# los tipos son Pago | Cargo
class TipoHistorico(models.Model):
	tipo_historico	= models.CharField(max_length=20)
	
	def __unicode__(self):
		return self.tipo_historico

class Historico(models.Model):
	cliente 		= models.ForeignKey(Cliente)
	datetime 		= models.DateTimeField(auto_now=True)
	cantidad 		= models.IntegerField()
	descripcion		= models.CharField(max_length=30)
	metodo_pago 	= models.ForeignKey(MetodoPago)
	tipo_historico	= models.ForeignKey(TipoHistorico)

