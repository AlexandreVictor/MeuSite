from django.db import models

# Create your models here.
class Tabela_Relatorios(models.Model):

    nome_relatorio = models.CharField('Nome Relatório', max_length = 150)
    ativo = models.IntegerField()
    criado_em = models.DateTimeField('Data Criação',auto_now=True)
    modificao_em = models.DateTimeField('Data Modificação',null = True)
    
    class Meta:
        db_table = 'GRT_tb_relatorios'

    def __str__(self):
        return self.nome_relatorio

class Tabela_Trilhas(models.Model):

    trilha = models.CharField(max_length = 150)
    plataforma = models.CharField(max_length = 50)
    codtrilha_legado = models.IntegerField(default=0,null = True)
    ativo = models.IntegerField(default=1)
    
    class Meta:
        db_table = 'GRT_tb_trilhas'
    
    def __str__(self):
      return self.trilha

class Tabela_Trilha_Relatorio(models.Model):
    
    fk_idrelatorio = models.ForeignKey(Tabela_Relatorios, on_delete=models.CASCADE)
    fk_idtrilha   = models.ForeignKey(Tabela_Trilhas, on_delete=models.CASCADE)
    ativo = models.IntegerField(default=1)

    class Meta:
        db_table = 'GRT_tb_trilha_relatorio'
        

class Cronograma_Controle(models.Model):

    data          = models.DateTimeField('Data do Relatório')
    data_ref      = models.DateTimeField('Data de Referência')
    atualizado_em = models.DateTimeField('Data da Atualização',null = True)
    fechamento    = models.IntegerField(default=0)
    fk_idtrilharelatorio = models.ForeignKey(Tabela_Trilha_Relatorio,on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'GRT_tb_cronograma_controle'