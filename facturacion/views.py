from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from facturacion.models import Proceso
from clientes.models import Cliente


from facturacion.forms import NuevoProceso




def lista_procesos(request):
	listaprocesos 	= Proceso.objects.all().order_by('fecha_facturacion').reverse()
	return render_to_response('facturacion/procesos.html', {'list': listaprocesos },context_instance=RequestContext(request))

def nuevo_proceso(request):
	if request.method=='POST':
		form = NuevoProceso(request.POST, initial={'status': 'Inicio'})
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/facturar')
	else:
		form = NuevoProceso(initial={'status': 'Inicio'})

	return render_to_response('facturacion/nuevo_proceso.html',{'form':form}, context_instance=RequestContext(request))


def facturar(request):
	lista_clientes = Cliente.objects.all()
	return render_to_response('facturacion/facturar.html', {'list': lista_clientes}, context_instance=RequestContext(request))


def cambiar_plan(request,username):
	return HttpResponseRedirect('/facturar')



def generar_cobro(request):
	return HttpResponseRedirect('/resumen')


def resumen(request, id):	
	return render_to_response('facturacion/resumen.html', context_instance=RequestContext(request))


def boleta(request):
	return render_to_response('facturacion/boleta.html', context_instance=RequestContext(request))

