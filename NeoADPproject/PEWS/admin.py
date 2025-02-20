from django.contrib import admin
from . models import profissional_de_saude, paciente_crianca
# Register your models here.

class PDSadmin(admin.ModelAdmin):
    list_display = ('nome', 'crm', 'coren')
    
class PCadmin(admin.ModelAdmin):
    list_display = ('nome', 'data_de_nascimento')

admin.site.register(profissional_de_saude, PDSadmin)
admin.site.register(paciente_crianca, PCadmin)