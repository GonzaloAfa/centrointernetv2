from django.db import models


CLIENTE_STATUS = (
	('Activo','Activo'),
	('Moroso','Moroso'),
	('Cortado','Cortado'),
	('Anulado','Anulado'),

	)

RED = (
	('Z7','Z7.CentroInternet'),
	)

# Create your models here.
class Servicio(models.Model):
	plan			= models.CharField(max_length=20)
	detalle			= models.TextField()
	precio			= models.IntegerField()

	def __unicode__(self):
		return self.plan



class Cliente(models.Model):

	username		= models.CharField(max_length=20, unique=True)
	nombre 			= models.CharField(max_length=20)
	apellido		= models.CharField(max_length=30)

	rut				= models.CharField(max_length=15)
	direccion		= models.TextField()

	servicio 		= models.ForeignKey(Servicio)
	status 			= models.CharField(max_length=20, choices=CLIENTE_STATUS)
	red 			= models.CharField(max_length=20, choices=RED)

	email			= models.EmailField()
	celular			= models.CharField(max_length=15, help_text="Ejemplo: +56 9 xxxx xxxx")

	date_start		= models.DateTimeField(auto_now=True)


	def __unicode__(self):
		return self.username