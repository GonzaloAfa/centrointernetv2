from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()


urlpatterns = patterns('',
	url(r'^$','centrointernet.views.user_login'),
	url(r'^login/$','centrointernet.views.user_login'),

	url(r'^inicio/$','centrointernet.views.inicio'),
	url(r'^logout/$', 'centrointernet.views.cerrar'),

	url(r'^cliente/$','clientes.views.clientes'),
	url(r'^cliente/page/(?P<page>\d+)$','clientes.views.lista_clientes'),
	url(r'^cliente/nuevo/$','clientes.views.nuevo_cliente'),
	url(r'^perfil/(?P<username>\w+)$','clientes.views.perfil_cliente'),
	url(r'^perfil/editar/(?P<username>\w+)$','clientes.views.modificar_cliente'),
	
	
	url(r'^problema/$','problemas.views.problemas'),
	url(r'^problema/page/(?P<page>\d+)$','problemas.views.lista_problemas'),
	url(r'^problema/nuevo$','problemas.views.nuevo_problema'),
	url(r'^problema/detalle/(?P<id_problem>\d+)$','problemas.views.detalle_problema'),
	url(r'^problema/editar/(?P<id_problem>\d+)$','problemas.views.modificar_problema'),
	
	url(r'^pago/$','pagos.views.pagos'),
	url(r'^pago/nuevo$','pagos.views.nuevo_pago'),
	url(r'^pago/page/(?P<page>\d+)$','pagos.views.lista_pagos'),
	

	url(r'^proceso/$', 'facturacion.views.lista_procesos'),
	url(r'^proceso/nuevo$', 'facturacion.views.nuevo_proceso'),	
	url(r'^resumen/(?P<id>\d+)$', 'facturacion.views.resumen'),
	url(r'^boleta/$', 'facturacion.views.boleta'),
	url(r'^facturar/$', 'facturacion.views.facturar'),
	url(r'^facturar/generar_cobro$', 'facturacion.views.generar_cobro'),

	url(r'^generarPdf/(?P<id>\d+)$', 'facturacion.views.generar_pdf'),
	url(r'^enviarMail/(?P<id>\d+)$', 'facturacion.views.enviar_mail'),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
	
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

