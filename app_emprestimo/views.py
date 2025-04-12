from django.shortcuts import render, redirect
from app_emprestimo.models import ColaboradorModel, GerenteModel, EPIModel, EmprestimoModel
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'app_emprestimo/pages/home.html')

def cadastrar_equipamento(request):
    if request.method == 'GET':
        return render(request, 'app_emprestimo/pages/cadastrar_equipamento.html')
    

    nome = request.POST.get('nome')

    erro = None
    mensagem = None

    if EPIModel.objects.filter(nome=nome).exists():
        mensagem = "Equipamento ja cadastrado"
        erro = True
        return render(request, 'app_emprestimo/pages/cadastrar_equipamento.html', context={'erro':erro, 'mensagem':mensagem})
    else:
        mensagem = "Equipamento cadastrado com sucesso"
        erro = False
        descricao = request.POST.get('descricao')
        quantidade_total = request.POST.get('quantidade_total')
        epi = EPIModel.objects.create(nome=nome, descricao=descricao, quantidade_total=quantidade_total)
    return render(request, 'app_emprestimo/pages/cadastrar_equipamento.html', context={'erro':erro, 'mensagem':mensagem})
    
def listar_equipamento(request):
    equipamentos = EPIModel.objects.all()
    return render(request, 'app_emprestimo/pages/listar_equipamento.html', context={'equipamentos':equipamentos})

def atualizar_equipamento(request, idEPI):
    if request.method == 'GET':
        epi = EPIModel.objects.get(idEPI=idEPI)
        return render(request, 'app_emprestimo/pages/atualizar_equipamento.html', context={'epi':epi})
    
    nome = request.POST.get('nome')
    descricao = request.POST.get('descricao')
    quantidade_total = request.POST.get('quantidade_total')
    EPIModel.objects.filter(idEPI=idEPI).update(nome=nome, descricao=descricao, quantidade_total=quantidade_total)
    return redirect('listar_equipamento')

def deletar_equipamento(request, idEPI):
    epi = EPIModel.objects.get(idEPI=idEPI)
    epi.delete()
    return redirect('listar_equipamento')

def cadastrar_emprestimo(request):
    if request.method == 'POST':
        try:
            emprestimo = EmprestimoModel(
                idCOLABORADOR_id=request.POST.get('idCOLABORADOR'),
                idEPI_id=request.POST.get('idEPI'),
                data_emprestimo=request.POST.get('data_emprestimo'),
                data_devolucao_prevista=request.POST.get('data_devolucao_prevista'),
                status=request.POST.get('status'),
                observacao=request.POST.get('observacao', '')
            )
            emprestimo.full_clean()
            emprestimo.save()
            messages.success(request, 'Empréstimo cadastrado com sucesso!')
        except Exception as e:
            messages.error(request, f'Erro ao cadastrar empréstimo: {str(e)}')
    
    context = {
        'colaboradores': ColaboradorModel.objects.all(),
        'epis': EPIModel.objects.all(),
        'status_choices': EmprestimoModel.STATUS_CHOICE
    }
    return render(request, 'app_emprestimo/pages/cadastrar_emprestimo.html', context)



@login_required
def cadastro_gerente(request):
    if request.method == 'GET':
        return render(request, 'app_emprestimo/pages/cadastrar_gerente.html')
    
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    senha = request.POST.get('senha')
    gerente = GerenteModel.objects.create(nome=nome, cpf=cpf, senha=senha)
    return render(request, 'app_emprestimo/pages/cadastrar_gerente.html')

def cadastrar_colaborador(request):
    if request.method == 'GET':
        return render(request, 'app_emprestimo/pages/cadastrar_colaborador.html')
    

    cpf = request.POST.get('cpf')

    erro = None
    mensagem = None

    if ColaboradorModel.objects.filter(cpf=cpf).exists():
        mensagem = "Colaborador ja cadastrado"
        erro = True
        return render(request, 'app_emprestimo/pages/cadastrar_colaborador.html', context={'erro':erro, 'mensagem':mensagem})
    else:
        mensagem = "Colaborador cadastrado com sucesso"
        erro = False
        nome = request.POST.get('nome')
        funcao = request.POST.get('funcao')
        data_admissao = request.POST.get('data_admissao')
        colaborador = ColaboradorModel.objects.create(nome=nome, cpf=cpf, funcao=funcao, data_admissao=data_admissao)
    return render(request, 'app_emprestimo/pages/cadastrar_colaborador.html', context={'erro':erro, 'mensagem':mensagem})

def login_request(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        password = request.POST.get('password')
        
        gerente = authenticate(request, cpf=cpf, password=password)

        if gerente is not None:
            login(request, gerente)
            return redirect('home')
    return render(request, 'app_emprestimo/pages/login.html')



def deletar_colaborador(request, idCOLABORADOR):
    colaborador = ColaboradorModel.objects.get(idCOLABORADOR=idCOLABORADOR)
    colaborador.delete()
    return redirect('listar_colaboradores')


def listar_colaborador(request):
    pesquisa = request.GET.get('busca')
    if pesquisa:
        lista_emprestimo = EmprestimoModel.objects.filter(idCOLABORADOR__nome__icontains=pesquisa)
    else:
        lista_emprestimo = EmprestimoModel.objects.all()
    return render(request, 'app_emprestimo/pages/listar_colaborador.html', context={'emprestimos':lista_emprestimo, 'pesquisa':pesquisa})


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