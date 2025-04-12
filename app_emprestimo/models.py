from django.db import models


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