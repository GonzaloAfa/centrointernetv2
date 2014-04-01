from django.shortcuts import render


from clientes.models import Red
from clientes.models import Servicio
from clientes.models import ClienteStatus
from clientes.models import Cliente

from problemas.models import Problema
from pagos.models import Historico


from clientes.forms import NuevoCliente

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import InvalidPage


from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def clientes(request):
    return HttpResponseRedirect('/cliente/page/1')


def lista_clientes(request, page):
    listaclientes = Cliente.objects.all().order_by('date_start').reverse()
    paginator = Paginator(listaclientes,3)
    try:
        pages = int(page)
    except:
        pages = 1

    try:
        clientes = paginator.page(pages)

    except (InvalidPage):
        clientes = paginator.page(paginator.num_pages)

    return render_to_response('client/list.html',{'list':clientes}, context_instance=RequestContext(request))


def nuevo_cliente(request):
    if request.method=='POST':
        form = NuevoCliente(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/cliente')
    else:
        form = NuevoCliente()
    return render_to_response('client/new.html',{'form':form}, context_instance=RequestContext(request))


def perfil_cliente(request, username):
    cliente     = get_object_or_404(Cliente, username = username)
    problema    = Problema.objects.filter(cliente=cliente)[:5]
    historico   = Historico.objects.filter(cliente=cliente)[:5]
    return render_to_response('client/profile.html',
        {'cliente': cliente, 'problemas': problema, 'historico':historico},context_instance=RequestContext(request))

# 
