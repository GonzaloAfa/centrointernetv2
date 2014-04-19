from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from cupones.forms import NuevoProceso


def proceso(request):
	return render_to_response('coupon/procesos.html', context_instance=RequestContext(request))

def nuevo_proceso(request):
	if request.method=='POST':
		form = NuevoProceso(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/mensualidad')
	else:
		form = NuevoProceso(initial={'status': 'Inicio'})

	return render_to_response('coupon/nuevo_proceso.html',{'form':form}, context_instance=RequestContext(request))



def boleta(request):
	return render_to_response('coupon/boleta.html', context_instance=RequestContext(request))

def resumen(request):
	return render_to_response('coupon/resumen.html', context_instance=RequestContext(request))

def mensualidad(request):
	return render_to_response('coupon/mensualidad.html', context_instance=RequestContext(request))
