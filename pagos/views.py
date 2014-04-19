from django.shortcuts import render


from pagos.models import Historico

from pagos.models import PAGO, COBRO, DESCUENTO

from pagos.forms import NuevoPago

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
    listapagos = Historico.objects.filter(tipo_historico = PAGO ).order_by('datetime').reverse()
    paginator = Paginator(listapagos,3)
    try:
        pages = int(page)
    except:
        pages = 1

    try:
        pagos = paginator.page(pages)

    except (InvalidPage):
        listapagos = paginator.page(paginator.num_pages)

    return render_to_response('pay/list.html',{'list':pagos}, context_instance=RequestContext(request))


def nuevo_pago(request):
    if request.method=='POST':
        form = NuevoPago(request.POST, request.FILES, initial={'tipo_historico' : 'Pago'},)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pago')
    else:
        form = NuevoPago()
    return render_to_response('pay/new.html',{'form':form}, context_instance=RequestContext(request))

