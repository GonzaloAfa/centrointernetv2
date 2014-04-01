#encoding:utf-8
from django.db import models

class Service(models.Model):
	plan			= models.CharField(max_length=20)
	detail			= models.TextField()
	price			= models.IntegerField()

	def __unicode__(self):
		return self.plan

class ClientStatus(models.Model):
	status 			= models.CharField(max_length=20)
	def __unicode__(self):
		return self.status

class NetworkConnection(models.Model):
	network 		= models.CharField(max_length=20)

	def __unicode__(self):
		return self.network


class Client(models.Model):

	username		= models.CharField(max_length=20)
	first_name 		= models.CharField(max_length=20)
	last_name		= models.CharField(max_length=30)

	rut				= models.CharField(max_length=15)
	address			= models.TextField()

#	GENDER_CHOICES 	= ( ('M', 'Male'), ('F', 'Female'), )
#	gender 			= models.CharField( max_length =1, choices=GENDER_CHOICES)

	service 		= models.ForeignKey(Service)
	status 			= models.ForeignKey(ClientStatus)
	network_connection=	models.ForeignKey(NetworkConnection)

	email			= models.EmailField()
	phone			= models.CharField(max_length=20, help_text="Ejemplo: +56 9 xxxx xxxx")

	georeferent		= models.TextField()
	date_start		= models.DateTimeField(auto_now=True)


	def __unicode__(self):
		return self.username

class TypeProblem(models.Model):
	type_problem	= models.CharField(max_length=20)

	def __unicode__(self):
		return self.type_problem

class ProblemStatus(models.Model):
	status	= models.CharField(max_length=20)

	def __unicode__(self):
		return self.status

class Problem (models.Model):
	client 			= models.ForeignKey(Client)
	problem_type 	= models.ForeignKey(TypeProblem)
	comment 		= models.TextField()
	datetime 		= models.DateTimeField(auto_now=True)
	status 			= models.ForeignKey(ProblemStatus)
	discount		= models.IntegerField()

class MethodPayment(models.Model):
	method 			= models.CharField(max_length=20)

	def __unicode__(self):
		return self.method

class TypeHistorical(models.Model):
	type_historical	= models.CharField(max_length=20)
	
	def __unicode__(self):
		return self.type_historical

class Historical(models.Model):
	client 			= models.ForeignKey(Client)
	datetime 		= models.DateTimeField(auto_now=True)
	amount 			= models.IntegerField()
	description		= models.CharField(max_length=30)
	method_payment 	= models.ForeignKey(MethodPayment)
	type_historical	= models.ForeignKey(TypeHistorical)
