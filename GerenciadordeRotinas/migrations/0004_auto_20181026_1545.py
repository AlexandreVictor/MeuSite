# Generated by Django 2.1.2 on 2018-10-26 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GerenciadordeRotinas', '0003_auto_20181023_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabela_relatorios',
            name='ativo',
            field=models.IntegerField(),
        ),
    ]