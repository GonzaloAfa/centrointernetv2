#encoding:utf-8
from django.db import models

from clientes.models import Cliente

# Create your models here.
TIPO_MES = (
	('Enero','Enero'),
	('Febrero','Febrero'),
	('Marzo','Marzo'),
	('Abril','Abril'),
	('Mayo','Mayo'),
	('Junio','Junio'),
	('Julio','Julio'),
	('Agosto','Agosto'),
	('Septiembre','Septiembre'),
	('Octubre','Octubre'),
	('Noviembre','Noviembre'),
	('Diciembre','Diciembre'),
	
	)

TIPO_ANO = (
	('2014','2014'),
	)

TIPO_STATUS = (
	('Inicio','Inicio'),
	('Facturar','Facturar'),
	('Resumen','Resumen'),
	('Email Enviado','Email Enviado'),
	('Archivado','Archivado'),
	)


class Proceso(models.Model):

	ano					= models.CharField(max_length=20,choices=TIPO_ANO)
	mes 				= models.CharField(max_length=20,choices=TIPO_MES)
	periodo_inicio 		= models.DateField(max_length=20)
	periodo_termino		= models.CharField(max_length=20)
	fecha_corte			= models.CharField(max_length=20)
	fecha_facturacion 	= models.DateTimeField(auto_now=True)
	status 				= models.CharField(max_length=20,choices=TIPO_STATUS, default='Inicio')

	def __unicode__(self):
		return self.ano + " "+ self.mes

class ResumenBoleta(models.Model):
	proceso 		= models.ForeignKey(Proceso)
	usuario			= models.ForeignKey(Cliente)
	estado_usuario 	= models.CharField(max_length=20)
	plan			= models.CharField(max_length=20)
	total			= models.CharField(max_length=20)
