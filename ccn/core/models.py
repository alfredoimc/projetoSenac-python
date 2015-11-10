from django.db import models

from django.contrib.auth.models import User

# Create your models here.



class UserProfile(models.Model):
	user = models.OneToOneField(User)
	telefone = models.CharField(u'Celular', max_length=14, help_text='(99)99999-9999')
	foto = models.ImageField(upload_to="media/profile", blank=True)
	data_cadastro = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "%s %s" % (self.user.first_name, self.user.last_name)


class noticias(models.Model):
	titulo = models.CharField(u'Noticia', max_length=100)
	descricao = models.TextField(u'Finalidade')
	data_noticia = models.DateField(u'Data')
	horario = models.TimeField(u'Horario')
	imagem = models.ImageField(u'Imagem')
	data_criacao = models.DateTimeField(auto_now_add=True)