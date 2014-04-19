from django.db import models


CLIENTE_STATUS = (
	('Activo','Activo'),
	('Moroso','Moroso'),
	('Cortado','Cortado'),
	('Anulado','Anulado'),

	)

# Create your models here.
class Servicio(models.Model):

	plan			= models.CharField(max_length=20)
	detalle			= models.TextField()
	precio			= models.IntegerField()

	def __unicode__(self):
		return self.plan

class ClienteStatus(models.Model):
	status 			= models.CharField(max_length=20, choices=CLIENTE_STATUS)
	def __unicode__(self):
		return self.status

class Red(models.Model):
	red 		= models.CharField(max_length=20)
	def __unicode__(self):
		return self.red


class Cliente(models.Model):

	username		= models.CharField(max_length=20)
	nombre 			= models.CharField(max_length=20)
	apellido		= models.CharField(max_length=30)

	rut				= models.CharField(max_length=15)
	direccion		= models.TextField()

	servicio 		= models.ForeignKey(Servicio)
	status 			= models.ForeignKey(ClienteStatus)
	red 			= models.ForeignKey(Red)

	email			= models.EmailField()
	celular			= models.CharField(max_length=20, help_text="Ejemplo: +56 9 xxxx xxxx")

	date_start		= models.DateTimeField(auto_now=True)


	def __unicode__(self):
		return self.username