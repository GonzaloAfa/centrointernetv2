#encoding:utf-8
from django.db import models

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
	('Mensualidad','Mensualidad'),
	('Resumen','Resumen'),
	('Envio Email','Envio Email'),


	)


class Proceso(models.Model):
	ano					= models.CharField(max_length=20,choices=TIPO_ANO)
	mes 				= models.CharField(max_length=20,choices=TIPO_MES)
	periodo_inicio 		= models.CharField(max_length=20)
	periodo_termino		= models.CharField(max_length=20)
	fecha_corte			= models.CharField(max_length=20)
	fecha_facturacion 	= models.DateTimeField(auto_now=True)
	status 				= models.CharField(max_length=20,choices=TIPO_STATUS)


class ResumenBoleta(models.Model):
	usuario		= models.CharField(max_length=20)