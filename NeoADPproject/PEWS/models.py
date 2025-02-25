from django.db import models


# Create your models here.
class profissional_de_saude(models.Model):
    cpf = models.CharField(primary_key=1, max_length=16)
    crm = models.CharField(max_length=16, unique=1, null=1)
    coren = models.CharField(max_length=16, unique=1, null=1)
    nome = models.CharField(max_length=64)
    telefone = models.CharField(max_length=16)
    senha = models.CharField(max_length=16)


class paciente_crianca(models.Model):
    matricula = models.IntegerField()
    nome = models.CharField(max_length=32)
    data_de_nascimento = models.DateField()


