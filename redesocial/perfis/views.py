from django.shortcuts import render, redirect
from .models import Perfil, Convite
# Create your views here.

def index(request):
	return render(request, 'index.html',
		          {'perfis': Perfil.objects.all(),
                   'perfil_logado' : get_perfil_logado(request)})

def exibir(request, perfil_id):
	return render(request, 'perfil.html',
		          {'perfil' : Perfil,
                   'perfil_logado' : get_perfil_logado(request)})

def convidar(request, perfil_id):
	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.convidar(perfil_a_convidar)
	return redirect('index')

def get_perfil_logado(request):
	return Perfil.objects.get(id=1)

def aceitar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('index')
