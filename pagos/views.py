from django.shortcuts import render


from pagos.models import Historico
from clientes.models import Cliente

from pagos.models import PAGO, COBRO, DESCUENTO

from pagos.forms import NuevoPago
from pagos.forms import NuevoCobro
from pagos.forms import NuevoDescuento

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import InvalidPage


from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def pagos(request):
    return HttpResponseRedirect('/pago/page/1')


def lista_pagos(request, page):
    listapagos = Historico.objects.filter( tipo_historico = PAGO ).order_by('datetime').reverse()
    paginator = Paginator(listapagos,3)
    try:
        pages = int(page)
    except:
        pages = 1

    try:
        pagos = paginator.page(pages)

    except (InvalidPage):
        listapagos = paginator.page(paginator.num_pages)

    return render_to_response('pay/list.html',{'list':listapagos}, context_instance=RequestContext(request))


def nuevo_pago(request):
    if request.method=='POST':
        form = NuevoPago(request.POST, request.FILES , initial={'tipo_historico' : PAGO},)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pago')
    else:
        form = NuevoPago(initial={'tipo_historico' : PAGO})
    return render_to_response('pay/new.html',{'form':form}, context_instance=RequestContext(request))

def nuevo_cobro(request, username):
    if request.method=='POST':
        cliente = Cliente.objects.filter(username=username).first()
        form = NuevoCobro(request.POST, initial={'tipo_historico' : COBRO, 'metodo_pago': 'Sucursal', 'cliente': cliente},)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/facturar/proceso/resumen')
    else:
        cliente = Cliente.objects.filter(username=username).first()
        form = NuevoCobro(initial={'tipo_historico' : COBRO, 'metodo_pago': 'Sucursal', 'cliente': cliente})
    return render_to_response('pay/new.html',{'form':form}, context_instance=RequestContext(request))

def nuevo_descuento(request, username):
    if request.method=='POST':
        cliente = Cliente.objects.filter(username=username).first()
        form = NuevoDescuento(request.POST, initial={'tipo_historico' : DESCUENTO, 'metodo_pago': 'Sucursal', 'cliente': cliente},)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/facturar/proceso/resumen')
    else:
        cliente = Cliente.objects.filter(username=username).first()
        form = NuevoDescuento(initial={'tipo_historico' : DESCUENTO, 'metodo_pago': 'Sucursal', 'cliente': cliente})
    return render_to_response('pay/new.html',{'form':form}, context_instance=RequestContext(request))