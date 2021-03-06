import pdb
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader, Context

from facturacion.models import Proceso
from facturacion.models import ResumenBoleta
from clientes.models import Cliente
from pagos.models import PAGO, COBRO, DESCUENTO
from pagos.models import Historico

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import InvalidPage

from facturacion.forms import NuevoProceso
from facturacion.utils import saveHtmlToPdf, send_mail_to_client, PDF_HTTP_Response

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from weasyprint import HTML, Document

#usar name url para redireccionar
from django.core.urlresolvers import reverse

from django.db.models import Q

@login_required()
def lista_procesos(request):
	listaprocesos 	= Proceso.objects.all().order_by('fecha_facturacion').reverse()
	return render_to_response('facturacion/procesos.html', {'list': listaprocesos },context_instance=RequestContext(request))

@login_required()
def nuevo_proceso(request):
	if request.method=='POST':
		form = NuevoProceso(request.POST, initial={'status': 'Inicio'})
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('listado_clientes'))
	else:
		form = NuevoProceso(initial={'status': 'Inicio'})

	return render_to_response('facturacion/nuevo_proceso.html',{'form':form}, context_instance=RequestContext(request))

@login_required()
def listado_clientes(request):
	lista_clientes = Cliente.objects.filter(status='Activo' or 'Moroso').order_by('username')
	return render_to_response('facturacion/listado_clientes.html',{'list':lista_clientes}, context_instance=RequestContext(request))

@login_required()
def generar_cobros(request):
	proceso = Proceso.objects.filter(status='Inicio').order_by('fecha_facturacion').reverse().first()
	
	if proceso is not None and proceso.status == 'Inicio':
		print proceso.status
		descripcion = proceso.mes + ' ' + proceso.ano  
		lista_clientes = Cliente.objects.filter(status='Activo' or 'Moroso').order_by('username')
		for cliente in lista_clientes:
			# Generamos el cobro mensual
			cobro = Historico(cliente=cliente, cantidad=cliente.servicio.precio, descripcion=descripcion , metodo_pago='Sucursal', tipo_historico=COBRO)
			cobro.save()
		# Cambia de estado a facturado
		proceso.status = 'Facturar'
		proceso.save()
		

	return HttpResponseRedirect(reverse('resumen'))

@login_required()
def listado_resumen(request):
	proceso = Proceso.objects.filter(Q(status='Facturar') | Q(status='Resumen') ).order_by('fecha_facturacion').reverse().first()
	lista_clientes = Cliente.objects.filter(Q(status='Activo') | Q(status='Moroso')).order_by('username')

	# itera sobre los clientes para calcular el total a pagar
	for cliente in lista_clientes:
		lista_pagos = Historico.objects.filter(cliente=cliente)
		total = 0
		for pago in lista_pagos:
			if pago.tipo_historico == PAGO:
				total -= pago.cantidad
			elif pago.tipo_historico == COBRO:
				total += pago.cantidad
			elif pago.tipo_historico == DESCUENTO:
				total -= pago.cantidad
		cliente.total = total
		# Crea el resumen de la boleta
		if proceso is not None:
			resumen_boleta = ResumenBoleta(proceso=proceso, usuario=cliente, estado_usuario=cliente.status, plan=cliente.servicio.plan, total= total)
			resumen_boleta.save()
	if proceso is not None:
		proceso.status = 'Resumen'
		proceso.save()
	return render_to_response('facturacion/listado_resumen.html', {'list':lista_clientes, 'proceso': proceso}, context_instance=RequestContext(request))

@login_required()
def boleta(request, username):
	cliente 	= get_object_or_404(Cliente, username = username)
	historico   = Historico.objects.filter(cliente=cliente)[:10]
	proceso 	= Proceso.objects.filter(status='Resumen').order_by('fecha_facturacion').reverse().first()	
	resumen_boleta 	= ResumenBoleta.objects.filter(proceso=proceso, usuario=cliente).reverse().first()
	
	print resumen_boleta
	return render_to_response('facturacion/boleta.html',
		{'cliente': cliente, 'historico': historico, 'proceso': proceso, 'resumen_boleta': resumen_boleta},
		 context_instance=RequestContext(request))


@login_required()
def generar_pdfs(request):
	lista_clientes = Cliente.objects.filter(Q(status='Activo') | Q(status='Moroso')).order_by('username')
	proceso 	= Proceso.objects.filter(status='Resumen').order_by('fecha_facturacion').reverse().first()	
	lista_boletas = []
	for cliente in lista_clientes:
		historico   = Historico.objects.filter(cliente=cliente)[:10]
		resumen_boleta 	= ResumenBoleta.objects.filter(proceso=proceso, usuario=cliente).reverse().first()
		boleta = render_to_response('facturacion/boleta2.html',
		{'cliente': cliente, 'historico': historico, 'proceso': proceso, 'resumen_boleta': resumen_boleta},
		 context_instance=RequestContext(request))

		html_boleta = boleta.content
		lista_boletas.append(HTML(string=html_boleta).render()) 

	paginas_boletas = [page for boleta in lista_boletas for page in boleta.pages]
	pdf = lista_boletas[0].copy(paginas_boletas).write_pdf()
	response = HttpResponse(pdf, mimetype='application/pdf')
	response['Content-Disposition'] = 'filename=Resumen '+proceso.ano+' '+proceso.mes+'.pdf'

	return response
	# return render_to_response('facturacion/facturar.html', context_instance=RequestContext(request))

@login_required()
def generar_pdf(request, id):
	template = loader.get_template('facturacion/boleta.html')
	context = RequestContext(request, {})
	html = template.render(context)
	filename = 'boleta.pdf'
	return PDF_HTTP_Response(html, filename)

@login_required()
def enviar_mail(request, id):
	template = loader.get_template('facturacion/boleta.html')
	context = RequestContext(request, {})
	html = template.render(context)
	
	filename = 'facturacion/boletas/boleta.pdf'
	email_cliente = 'testcentrointernet@gmail.com'
	titulo = 'titulo'
	content = 'contenido'

	saveHtmlToPdf(html, filename)
	send_mail_to_client(titulo, content, email_cliente, attachment=filename)
	return HttpResponseRedirect('/resumen/1')

    


