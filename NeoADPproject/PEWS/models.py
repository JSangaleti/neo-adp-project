from django.db import models

# Create your models here.
class profissional_de_saude(models.Model):
    id = models.IntegerField(primary_key=1, auto_created=1)
    crm = models.CharField(max_length=16, unique=1, null=1)
    coren = models.CharField(max_length=16, unique=1, null=1)
    nome = models.CharField(max_length=64)
    telefone = models.CharField(max_length=16)
    senha = models.CharField(max_length=16)