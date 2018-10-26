from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import *
from .models import *
from django.shortcuts import redirect
from django.views.generic import CreateView



def index(request):
    teste =  Tabela_Relatorios.objects.all()[:5]
    context = {'teste': teste}
    return render(request, 'GerenciadordeRotinas/index.html', context)


def relatorioslist(request):
    relatorios_list =  Tabela_Relatorios.objects.all()
    relatorios_qtd =  Tabela_Relatorios.objects.count()
    context = {'relatorios_list': relatorios_list,
               }
    return render(request, 'GerenciadordeRotinas/listarelatorios.html', context)

def edit(request,id):
    fields_list =  Tabela_Relatorios.objects.filter(pk=id)
    context = {'fields_list':fields_list,
        
        }
    return render(request, 'GerenciadordeRotinas/formEdit.html', context)


def post(request):
    errors = []
    if request.method == 'POST':
        form = RelatorioForm(request.POST)
        dados = form.data
        Relatorios = form.save(commit=False)
        if RelatorioForm.valida_nome(form, dados['nome_relatorio']) is False:
            print('Entrou no if')
            errors = []
            errors.append('O nome já está cadastrado')
            return render(request, 'GerenciadordeRotinas/Cad_Relatorio.html',{'form': RelatorioForm(),'errors': errors})
           


        #RelatorioForm.valida_nome(form, dados['nome_relatorio'])
        #if form.is_valid():
        
        

        #print(form.cleaned_data)            
        #Relatorios = form.save()

    else:
        form = RelatorioForm()
    return render(request, 'GerenciadordeRotinas/Cad_Relatorio.html', {'form': RelatorioForm()})


