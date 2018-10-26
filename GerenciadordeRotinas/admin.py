from django.contrib import admin
from .models import *
# Register your models here.



class relatorioAdmin(admin.ModelAdmin):

     model = Tabela_Relatorios
     fieldsets = [
        ('Dados Gerais', {'fields': [(('nome_relatorio','ativo','modificao_em'))]}),
            ]
     list_display = ['nome_relatorio','criado_em','ativo']
     list_filter = ['nome_relatorio', 'ativo']
     search_fields = [(('nome_relatorio'))]

     def modificao_em(self, obj):
         return obj.modificao_em
     modificao_em.empty_value_display = '???'


     
   # save_on_top = True

admin.site.register (Tabela_Relatorios, relatorioAdmin)

class trilhaAdmin(admin.ModelAdmin):

     model = Tabela_Trilhas
     #save_on_bottom = True




#admin.site.register(Tabela_Relatorios)
admin.site.register(Tabela_Trilhas,trilhaAdmin)

