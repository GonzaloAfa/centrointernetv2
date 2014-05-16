from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader, Context

from facturacion.models import Proceso
from clientes.models import Cliente


from facturacion.forms import NuevoProceso
from facturacion.utils import saveHtmlToPdf, send_mail_to_client, PDF_HTTP_Response

#usar name url para redireccionar
from django.core.urlresolvers import reverse


def lista_procesos(request):
	listaprocesos 	= Proceso.objects.all().order_by('fecha_facturacion').reverse()
	return render_to_response('facturacion/procesos.html', {'list': listaprocesos },context_instance=RequestContext(request))

def nuevo_proceso(request):
	if request.method=='POST':
		form = NuevoProceso(request.POST, initial={'status': 'Inicio'})
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('listado_clientes'))
	else:
		form = NuevoProceso(initial={'status': 'Inicio'})

	return render_to_response('facturacion/nuevo_proceso.html',{'form':form}, context_instance=RequestContext(request))


def listado_clientes(request):
	return render_to_response('facturacion/listado_clientes.html', context_instance=RequestContext(request))


def generar_cobros(request):
	return HttpResponseRedirect(reverse('resumen'))


def listado_resumen(request):	
	return render_to_response('facturacion/listado_resumen.html', context_instance=RequestContext(request))




def generar_pdfs(request):
	return render_to_response('facturacion/facturar.html', context_instance=RequestContext(request))



def generar_pdf(request, id):
	template = loader.get_template('facturacion/boleta.html')
	context = RequestContext(request, {})
	html = template.render(context)
	filename = 'boleta.pdf'
	return PDF_HTTP_Response(html, filename)

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
    
def boleta(request, username):
	return render_to_response('facturacion/boleta.html', context_instance=RequestContext(request))

