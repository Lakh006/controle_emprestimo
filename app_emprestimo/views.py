from django.shortcuts import render, redirect
from app_emprestimo.models import ColaboradorModel, GerenteModel, EPIModel, EmprestimoModel
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
# Retorna a pagina principal
def home(request):
    return render(request, 'app_emprestimo/pages/home.html')

#funcao para cadastrar equipamento
def cadastrar_equipamento(request):
    if request.method == 'GET': # Se o elemento for GET retorna a pagina
        return render(request, 'app_emprestimo/pages/cadastrar_equipamento.html')
    

    nome = request.POST.get('nome') # Variavel para armazenar o nome, para validar se o equipamento ja esta cadastrado

    erro = None # Variavel para armazenar o erro
    mensagem = None # Variavel para armazenar a mensagem

    if EPIModel.objects.filter(nome=nome).exists(): # Filtra o equipamento pelo nome, se for verdadeiro retorna erro
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
    
def listar_equipamento(request): # Funcao simples para retornar todos os equipamentos cadastrados no banco de dados
    equipamentos = EPIModel.objects.all()
    return render(request, 'app_emprestimo/pages/listar_equipamento.html', context={'equipamentos':equipamentos})

def atualizar_equipamento(request, idEPI): # Funcao para caso o equipamento seja atualizado
    if request.method == 'GET':
        epi = EPIModel.objects.get(idEPI=idEPI) # Variavel para pega o id do equipamento
        return render(request, 'app_emprestimo/pages/atualizar_equipamento.html', context={'epi':epi}) # Retorna a pagina, junto com o id
    #atualiza os dados necessarios do equipamento
    nome = request.POST.get('nome')
    descricao = request.POST.get('descricao')
    quantidade_total = request.POST.get('quantidade_total')
    EPIModel.objects.filter(idEPI=idEPI).update(nome=nome, descricao=descricao, quantidade_total=quantidade_total)
    return redirect('listar_equipamento') # Redireciona para a pagina de listar equipamentos

def deletar_equipamento(request, idEPI):
    epi = EPIModel.objects.get(idEPI=idEPI)
    epi.delete()
    return redirect('listar_equipamento')

def cadastrar_emprestimo(request):
    if request.method == 'POST': # Se o metodo for do tipo post tente:
        try:
            emprestimo = EmprestimoModel(
                idCOLABORADOR_id=request.POST.get('idCOLABORADOR'),
                idEPI_id=request.POST.get('idEPI'),
                data_emprestimo=request.POST.get('data_emprestimo'),
                data_devolucao_prevista=request.POST.get('data_devolucao_prevista'),
                status=request.POST.get('status'),
                observacao=request.POST.get('observacao', '')
            )
            emprestimo.full_clean() # Valida os dados do emprestimo, garantindo dados validos
            emprestimo.save() # Funcao para guardar os dados emprestimos no banco de dados
            messages.success(request, 'Empréstimo cadastrado com sucesso!') # Mensagem de sucesso
        except Exception as e: # Se ocorrer uma excecao
            messages.error(request, f'Erro ao cadastrar empréstimo: {str(e)}') # Mensagem de erro, juntamente com o erro encontrado
    
    context = {
        'colaboradores': ColaboradorModel.objects.all(),
        'epis': EPIModel.objects.all(),
        'status_choices': EmprestimoModel.STATUS_CHOICE
    } # Guarda em um diario para que essas informacoes possam ser colocadas na pagina
    return render(request, 'app_emprestimo/pages/cadastrar_emprestimo.html', context) # Retorna a pagina, juntamente com o context

def atualizar_emprestimo(request, idEMPRESTIMO): # Funcao para atualizar os emprestimos
    if request.method == 'GET':
        emprestimo = EmprestimoModel.objects.get(idEMPRESTIMO=idEMPRESTIMO)
        context = {
            'emprestimo': emprestimo,
            'colaboradores': ColaboradorModel.objects.all(),
            'epis': EPIModel.objects.all(),
            'status_choices': EmprestimoModel.STATUS_CHOICE
        }
        return render(request, 'app_emprestimo/pages/atualizar_emprestimo.html', context)
    
    emprestimo = EmprestimoModel.objects.get(idEMPRESTIMO=idEMPRESTIMO)
    emprestimo.idCOLABORADOR_id = request.POST.get('idCOLABORADOR')
    emprestimo.idEPI_id = request.POST.get('idEPI')
    emprestimo.data_emprestimo = request.POST.get('data_emprestimo')
    emprestimo.data_devolucao_prevista = request.POST.get('data_devolucao_prevista')
    emprestimo.data_devolucao_real = request.POST.get('data_devolucao_real')
    emprestimo.observacao = request.POST.get('observacao')
    emprestimo.status = request.POST.get('status')
    emprestimo.observacao = request.POST.get('observacao', '')
    emprestimo.save()
    return redirect('listar_relatorio') # Rertona para a pagina de listar emprestimos

# def deletar_emprestimo(request, idEMPRESTIMO):
#     emprestimo = EmprestimoModel.objects.get(idEMPRESTIMO=idEMPRESTIMO)
#     emprestimo.delete()
#     return redirect('listar_emprestimos')

@login_required # **** Terminar ****
def cadastro_gerente(request):
    if request.method == 'GET':
        return render(request, 'app_emprestimo/pages/cadastrar_gerente.html')
    
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    senha = request.POST.get('senha')
    gerente = GerenteModel.objects.create(nome=nome, cpf=cpf, senha=senha)
    return render(request, 'app_emprestimo/pages/cadastrar_gerente.html')

def cadastrar_colaborador(request): # Funcao para cadastrar colaboradores
    if request.method == 'GET':
        return render(request, 'app_emprestimo/pages/cadastrar_colaborador.html')
    
    cpf = request.POST.get('cpf')

    erro = None
    mensagem = None

    if ColaboradorModel.objects.filter(cpf=cpf).exists(): # Verifica se o cpf ja esta cadastrado no banco de dados
        mensagem = "Colaborador ja cadastrado"
        erro = True # Erro
        return render(request, 'app_emprestimo/pages/cadastrar_colaborador.html', context={'erro':erro, 'mensagem':mensagem})
    else:
        mensagem = "Colaborador cadastrado com sucesso"
        erro = False
        nome = request.POST.get('nome')
        funcao = request.POST.get('funcao')
        data_admissao = request.POST.get('data_admissao')
        colaborador = ColaboradorModel.objects.create(nome=nome, cpf=cpf, funcao=funcao, data_admissao=data_admissao)
    return render(request, 'app_emprestimo/pages/cadastrar_colaborador.html', context={'erro':erro, 'mensagem':mensagem})

def listar_colaborador(request):
    colaboradores = ColaboradorModel.objects.all()
    return render(request, 'app_emprestimo/pages/listar_colaborador.html', context={'colaboradores':colaboradores})

def deletar_colaborador(request, idCOLABORADOR):
    colaborador = ColaboradorModel.objects.get(idCOLABORADOR=idCOLABORADOR)
    colaborador.delete()
    return redirect('listar_colaborador')

def atualizar_colaborador(request, idCOLABORADOR):
    if request.method == 'GET':
        colaborador = ColaboradorModel.objects.get(idCOLABORADOR=idCOLABORADOR)
        return render(request, 'app_emprestimo/pages/atualizar_colaborador.html', context={'colaborador':colaborador})
    
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    funcao = request.POST.get('funcao')
    data_admissao = request.POST.get('data_admissao')
    ColaboradorModel.objects.filter(idCOLABORADOR=idCOLABORADOR).update(nome=nome, cpf=cpf, funcao=funcao, data_admissao=data_admissao)
    return redirect('listar_colaborador')

def login_request(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        password = request.POST.get('password')
        
        gerente = authenticate(request, cpf=cpf, password=password)

        if gerente is not None:
            login(request, gerente)
            return redirect('home')
    return render(request, 'app_emprestimo/pages/login.html')


def listar_relatorio(request):
    pesquisa = request.GET.get('busca')
    if pesquisa:
        lista_emprestimo = EmprestimoModel.objects.filter(idCOLABORADOR__nome__icontains=pesquisa)
    else:
        lista_emprestimo = EmprestimoModel.objects.all()
    return render(request, 'app_emprestimo/pages/listar_relatorio.html', context={'emprestimos':lista_emprestimo, 'pesquisa':pesquisa})


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