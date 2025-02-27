from django.contrib import admin
from .models import (
    paciente_crianca,
    profissional_de_saude,
    responsavel_crianca,
    internacao,
)

# Register your models here.


class PDSadmin(admin.ModelAdmin):
    list_display = ("nome", "crm", "coren")


class PCadmin(admin.ModelAdmin):
    list_display = ("nome", "data_de_nascimento")


class RCadmin(admin.ModelAdmin):
    list_display = ("nome", "telefone", "cpf")


class internacao_admin(admin.ModelAdmin):
    list_display = ("leito", "paciente_crianca_matricula")


admin.site.register(profissional_de_saude, PDSadmin)
admin.site.register(paciente_crianca, PCadmin)
admin.site.register(responsavel_crianca, RCadmin)
admin.site.register(internacao, internacao_admin)
