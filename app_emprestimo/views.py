from django.shortcuts import render
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

    colaboradores = ColaboradorModel.objects.all()
    return render(request, 'app_emprestimo/pages/cadastrar.html', context={'colaboradores':colaboradores}) 

