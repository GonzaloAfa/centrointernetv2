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

	url(r'^cobro/nuevo/(?P<username>\w+)$','pagos.views.nuevo_cobro'),
	url(r'^descuento/nuevo/(?P<username>\w+)$','pagos.views.nuevo_descuento'),
	

	url(r'^facturar/$', 'facturacion.views.lista_procesos'),
	url(r'^facturar/proceso/nuevo$', 'facturacion.views.nuevo_proceso', name='inicio'),	
	url(r'^facturar/proceso/clientes$', 'facturacion.views.listado_clientes', name='listado_clientes'),
	url(r'^facturar/proceso/generar/cobros$', 'facturacion.views.generar_cobros', name='generar_cobros'),
	url(r'^facturar/proceso/resumen/$', 'facturacion.views.listado_resumen', name='resumen'),



	url(r'^facturar/proceso/generar/PDFs/(?P<id>\d+)$', 'facturacion.views.generar_pdf', name='generar_pdfs'),

	url(r'^facturar/PDF/descargar/(?P<id>\d+)$', 'facturacion.views.generar_pdf', name='generar_pdf'),
	url(r'^facturar/email/enviar/(?P<id>\d+)$', 'facturacion.views.enviar_mail'),

	url(r'^facturar/boleta/ver/(?P<username>\w+)$', 'facturacion.views.boleta'),



    url(r'^admin/', include(admin.site.urls)),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
	
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

