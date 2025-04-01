from django.db import models


# Create your models here.
class ColaboradorModel(models.Model):
    idCOLABORADOR = models.AutoField(primary_key=True)  
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    funcao = models.CharField(max_length=50)
    data_admissao = models.DateField()

    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Colaborador({self.nome}, {self.cpf}, {self.funcao})"
