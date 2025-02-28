from django.db import models


# Create your models here.


class profissional_de_saude(models.Model):
    cpf = models.CharField(primary_key=1, max_length=16)
    crm = models.CharField(max_length=16, unique=1, null=1)
    coren = models.CharField(max_length=16, unique=1, null=1)
    nome = models.CharField(max_length=64)
    telefone = models.CharField(max_length=16)
    senha = models.CharField(max_length=16)

    def __str__(self):
        return self.cpf


class paciente_crianca(models.Model):
    matricula = models.IntegerField()
    nome = models.CharField(max_length=32)
    data_de_nascimento = models.DateField()


class responsavel_crianca(models.Model):
    cpf = models.CharField(primary_key=1, max_length=16)
    nome = models.CharField(max_length=64)
    telefone = models.CharField(max_length=16)


class internacao(models.Model):
    protocolo = models.IntegerField(primary_key=1)
    paciente_crianca_matricula = models.IntegerField(
        models.ForeignKey(
            "PEWS.paciente_crianca", verbose_name=(""), on_delete=models.CASCADE
        )
    )
    leito = models.CharField(max_length=16)
    dih = models.FloatField()


class relatorio_pews(models.Model):
    relatorio_id = models.IntegerField(primary_key=1, auto_created=1)
    internacao_protocolo = models.IntegerField(
        models.ForeignKey(
            "PEWS.internacao", verbose_name=(""), on_delete=models.CASCADE
        )
    )
    pontuacao_pews = models.IntegerField()
    horario = models.DateTimeField()
