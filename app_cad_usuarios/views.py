from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')
def usuarios(request):
    # SALVAR OS DADOS DA TELA PARA O BANCO DE DADOS
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    # EXIBIR TODOS OS USUÁRIOS JA CADRASTADOS EM UMA NOVA PÁGINA   
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    # RETORNAR OS DADOS PARA A PÁGINA DE LISTAGEM DE USUÁRIOS
    return render(request,'usuarios/usuarios.html', usuarios)