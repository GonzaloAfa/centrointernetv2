from django.shortcuts import render

from problemas.models import Problema
from clientes.models import Cliente

# Create your views here.

from problemas.forms import NuevoProblema
from problemas.forms import EditarProblema


from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import InvalidPage


from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def problemas(request):
    return HttpResponseRedirect('/problema/page/1')


def lista_problemas(request, page):
    listaproblemas = Problema.objects.all().order_by('datetime').reverse()
    paginator = Paginator(listaproblemas,3)
    try:
        pages = int(page)
    except:
        pages = 1

    try:
        problemas = paginator.page(pages)

    except (InvalidPage):
        problemas = paginator.page(paginator.num_pages)

    return render_to_response('problem/list.html',{'list':problemas}, context_instance=RequestContext(request))

def nuevo_problema(request):
    if request.method=='POST':
        form = NuevoProblema(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/problema')
    else:
        form = NuevoProblema()
    return render_to_response('problem/new.html',{'form':form}, context_instance=RequestContext(request))



def detalle_problema(request, id_problem):
    problema         = get_object_or_404(Problema, id = id_problem)
    cliente          = get_object_or_404(Cliente, username=problema.cliente)
    lista_problemas  = Problema.objects.filter(cliente = problema.cliente).order_by('datetime').reverse()[:5]
    
    return render_to_response('problem/detail.html', 
        {'problem': problema, 'client': cliente, 'list_problem': lista_problemas},
         context_instance=RequestContext(request))


def modificar_problema(request, id_problem):
    p         = get_object_or_404(Problema, id = id_problem)

    if request.method=='POST':
        form    = EditarProblema(request.POST, request.FILES)
        if form.is_valid():

            p.comentario    = form.cleaned_data['comentario']
            p.status        = form.cleaned_data['status']
            p.descuento     = form.cleaned_data['descuento']

            p.save()
            return HttpResponseRedirect('/problema')

    if request.method == 'GET':
        form    = EditarProblema(initial = { 
            'comentario'    : p.comentario,
            'status'        : p.status,
            'descuento'     : p.descuento,
            })

    return render_to_response('problem/new.html',{'form':form, 'problema': p}, context_instance=RequestContext(request))

