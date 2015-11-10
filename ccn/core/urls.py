from django.conf.urls import url

from ccn.core.views import home, fisica, matematica, quimica, bbiologia, lbiologia,\
 contatos, sucesso_usuario, cadastro_usuario

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^fisica/$', fisica, name='fisica'),
	url(r'^matematica/$', matematica, name='matematica'),
	url(r'^quimica/$', quimica, name='quimica'),
	url(r'^bbiologia/$', bbiologia, name='bbiologia'),
	url(r'^lbiologia/$', lbiologia, name='lbiologia'),	
	url(r'^contatos/$' , contatos, name='contatos' ),_
	url(r'^cadastro-usuario/$', cadastro_usuario, name='cadastrousuario'),
	url(r'^sucesso-usuario/$', sucesso_usuario, name='usuariosucesso'),
]