from problemas.models import Problema 
from clientes.models import Cliente 
from pagos.models	import Historico

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import InvalidPage

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required



@login_required()
def inicio(request):
    clientes 	= Cliente.objects.all().order_by('date_start').reverse()[:5] 
    problemas 	= Problema.objects.all().order_by('datetime').reverse()[:5]
    pagos 		= Historico.objects.filter( tipo_historico = 'Pago').order_by('datetime').reverse()[:5]
    morosos 	= Cliente.objects.filter( status = 'Moroso').reverse()[:5] 

    return render_to_response('home/home.html', {'clients': clientes, 'problems': problemas , 'morosos': morosos, 'pays': pagos}, context_instance=RequestContext(request))

def user_login(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/inicio')

	if request.method == 'POST':

		username = request.POST['username']
		password = request.POST['password']

		access = authenticate(username=username, password=password)

		if access is not None:
			if access.is_active:

				login(request, access)
				return HttpResponseRedirect('/inicio/')
			else:
				return HttpResponseRedirect('/')
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponseRedirect('/')

	else:
		return render_to_response('login.html', context_instance=RequestContext(request))

@login_required(login_url='/inicio')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')