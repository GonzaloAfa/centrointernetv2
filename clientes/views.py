from django.shortcuts import render


from clientes.models import Servicio
from clientes.models import Cliente

from problemas.models import Problema
from pagos.models import Historico


from clientes.forms import NuevoCliente
from clientes.forms import EditarCliente 


from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import InvalidPage


from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

@login_required()
def clientes(request):
    return HttpResponseRedirect('/cliente/page/1')

@login_required()
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

@login_required()
def nuevo_cliente(request):
    if request.method=='POST':
        form = NuevoCliente(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/cliente')
    else:
        form = NuevoCliente()
    return render_to_response('client/new.html',{'form':form}, context_instance=RequestContext(request))

@login_required()
def modificar_cliente(request, username):
    p = get_object_or_404(Cliente, username = username)

    if request.method == 'POST':
        form    = EditarCliente(request.POST, request.FILES)
        if form.is_valid():
#            p.username  = form.cleaned_data['username']
            p.nombre    = form.cleaned_data['nombre']
            p.apellido  = form.cleaned_data['apellido']

            p.rut       = form.cleaned_data['rut'] 
            p.direccion = form.cleaned_data['direccion']

            p.servicio  = form.cleaned_data['servicio']
            p.status    = form.cleaned_data['status'] 
            p.red       = form.cleaned_data['red']

            p.email     = form.cleaned_data['email']
            p.celular   = form.cleaned_data['celular'] 

            p.save()
            return HttpResponseRedirect('/cliente')
    if request.method == 'GET':
        form = EditarCliente(initial = {
 #           'username'      : p.username,
            'nombre'        : p.nombre,
            'apellido'      : p.apellido,

            'rut'           : p.rut,
            'direccion'     : p.direccion,

            'servicio'      : p.servicio,
            'status'        : p.status,
            'red'           : p.red,
            'email'         : p.email,
            'celular'       : p.celular,
            })

    return render_to_response('client/new.html',
        {'form':form}, context_instance=RequestContext(request))



@login_required()
def perfil_cliente(request, username):
    cliente     = get_object_or_404(Cliente, username = username)
    problema    = Problema.objects.filter(cliente=cliente)[:5]
    historico   = Historico.objects.filter(cliente=cliente)[:5]
    return render_to_response('client/profile.html',
        {'cliente': cliente, 'problemas': problema, 'historico':historico},context_instance=RequestContext(request))

