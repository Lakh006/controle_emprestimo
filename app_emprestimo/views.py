from django.shortcuts import render, redirect
from app_emprestimo.models import ColaboradorModel

# Create your views here.
def home(request):
    return render(request, 'app_emprestimo/pages/home.html')

def cadastrar_colaborador(request):
    if request.method == 'GET':
        return render(request, 'app_emprestimo/pages/cadastrar.html')
    
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    funcao = request.POST.get('funcao')
    data_admissao = request.POST.get('data_admissao')
    colaborador = ColaboradorModel.objects.create(nome=nome, cpf=cpf, funcao=funcao, data_admissao=data_admissao)
    return render(request, 'app_emprestimo/pages/cadastrar.html')


def deletar_colaborador(request, idCOLABORADOR):
    colaborador = ColaboradorModel.objects.get(idCOLABORADOR=idCOLABORADOR)
    colaborador.delete()
    return redirect('listar_colaboradores')


def listar_colaboradores(request):
    colaboradores = ColaboradorModel.objects.all()
    return render(request, 'app_emprestimo/pages/listar.html', context={'colaboradores':colaboradores})

def atualizar_colaborador(request, idCOLABORADOR):
    if request.method == 'GET':
        colaborador = ColaboradorModel.objects.get(idCOLABORADOR=idCOLABORADOR)
        return render(request, 'app_emprestimo/pages/atualizar_colaborador.html', context={'colaborador':colaborador})
    
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    funcao = request.POST.get('funcao')
    data_admissao = request.POST.get('data_admissao')
    ColaboradorModel.objects.filter(idCOLABORADOR=idCOLABORADOR).update(nome=nome, cpf=cpf, funcao=funcao, data_admissao=data_admissao)
    return redirect('listar_colaboradores')