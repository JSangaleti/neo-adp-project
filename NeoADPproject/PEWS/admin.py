from django.contrib import admin
from . models import paciente_crianca, profissional_de_saude, responsavel_crianca
# Register your models here.

class PDSadmin(admin.ModelAdmin):
    list_display = ('nome', 'crm', 'coren')
    
class PCadmin(admin.ModelAdmin):
    list_display = ('nome', 'data_de_nascimento')
    
class RCadmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'cpf')

admin.site.register(profissional_de_saude, PDSadmin)
admin.site.register(paciente_crianca, PCadmin)
admin.site.register(responsavel_crianca, RCadmin)