from django.contrib import admin
from . models import profissional_de_saude
# Register your models here.

class PDSadmin(admin.ModelAdmin):
    list_display = ('nome', 'crm', 'coren')

admin.site.register(profissional_de_saude, PDSadmin)