# -*- coding: utf-8 -*-
from .models import *
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *


class RelatorioForm(forms.ModelForm):
    
    ativo = forms.RadioSelect()
    nome_relatorio = forms.CharField(label='Nome do Relatório:')
    
    class Meta:
           model = Tabela_Relatorios
           # Campos que estarão no form
           fields =  ['nome_relatorio', 'ativo']
   
    def valida_nome(self, nome):
      nomerelatorio =  Tabela_Relatorios.objects.filter(nome_relatorio=nome).count()
      if nomerelatorio is None:
          print('validado com sucesso')
          return True    
      else:
           print('Não válido')
           self.adiciona_erro('O nome já está cadastrado') 
           return False
    
    def adiciona_erro(self, message):
        errors = []
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        print("Erros foram adicionados")
        errors.append(message)
