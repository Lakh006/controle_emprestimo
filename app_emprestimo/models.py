from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


# Create your models here.
class ColaboradorModel(models.Model):
    idCOLABORADOR = models.AutoField(primary_key=True)  
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    funcao = models.CharField(max_length=50)
    data_admissao = models.DateField()

    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Colaborador({self.nome}, {self.cpf}, {self.funcao})"

class GerenteModel(models.Model):
    idGERENTE = models.AutoField(primary_key=True)  
    nome = models.CharField(max_length=50)
    senha = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    
    def __str__(self):
        return f"Gerente({self.nome}"
    
class EPIModel(models.Model):
    idEPI = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    quantidade_total = models.IntegerField()
    
class EmprestimoModel(models.Model):
    idEMPRESTIMO = models.AutoField(primary_key=True)
    idCOLABORADOR = models.ForeignKey(ColaboradorModel, on_delete=models.CASCADE)
    idEPI = models.ForeignKey(EPIModel, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao_prevista = models.DateField()
    data_devolucao_real = models.DateField(null=True, blank=True)
    STATUS_CHOICE = (
        ('Emprestado', 'Emprestado'),
        ('Em uso', 'Em uso'),
        ('Fornecido', 'Forncecido'),
        ('Devolvido', 'Devolvido'),
        ('Danificado', 'Daificado'),
        ('Perdido', 'Perdido'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='Emprestado')   
    observacao = models.TextField(null=True, blank=True)
    
    def clean(self):
        # Converte timezone.now() para date antes de comparar
        if self.data_devolucao_prevista <= timezone.now().date():
            raise ValidationError("A data de devolução deve ser futura!")