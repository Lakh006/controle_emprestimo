from django.shortcuts import render, redirect
from app_emprestimo.models import ColaboradorModel, GerenteModel
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'app_emprestimo/pages/home.html')

@login_required
def cadastro_gerente(request):
    if request.method == 'GET':
        return render(request, 'app_emprestimo/pages/cadastrar_gerente.html')
    
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    senha = request.POST.get('senha')
    gerente = GerenteModel.objects.create(nome=nome, cpf=cpf, senha=senha)
    return render(request, 'app_emprestimo/pages/cadastrar_gerente.html')

def login_request(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        password = request.POST.get('password')
        
        gerente = authenticate(request, cpf=cpf, password=password)

        if gerente is not None:
            login(request, gerente)
            return redirect('home')
    return render(request, 'app_emprestimo/pages/login.html')

def cadastrar_colaborador(request):
    if request.method == 'GET':
        return render(request, 'app_emprestimo/pages/cadastrar_colaborador.html')
    
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    funcao = request.POST.get('funcao')
    data_admissao = request.POST.get('data_admissao')
    colaborador = ColaboradorModel.objects.create(nome=nome, cpf=cpf, funcao=funcao, data_admissao=data_admissao)
    return render(request, 'app_emprestimo/pages/cadastrar_colaborador.html')


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