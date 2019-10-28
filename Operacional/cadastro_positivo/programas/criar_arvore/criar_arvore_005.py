# import json


class Historico:
    def __init__(self):
        Historico.nome_reduzido = 'EnvoHstCrd'
        Historico.atributos = dict()
        
        Historico.clientes_min = 0
        Historico.clientes_max = 'ilimitado'
        Historico.clientes = list()

class Cliente:
    def __init__(self):
        Cliente.nome_reduzido = 'Cli'
        Cliente.atributos = dict()

        Cliente.operacoes_min = 0
        Cliente.operacoes_max = 'ilimitado'
        Cliente.operacoes = list()

class Operacao:
    def __init__(self):
        Operacao.nome_reduzido = 'Opr'
        Operacao.atributos = dict()

        Operacao.detalhe_operacoes_min = 0
        Operacao.detalhe_operacoes_max = 1
        Operacao.detalhe_operacoes = dict()

        Operacao.parcelas_anteriores_min = 0
        Operacao.parcelas_anteriores_max = 'ilimitado'
        Operacao.parcelas_anteriores = list()

        Operacao.pagamentos_avulsos_min = 0
        Operacao.pagamentos_avulsos_max = 'ilimitado'
        Operacao.pagamentos_avulsos = list()

        Operacao.parcelas_futuras_min = 0
        Operacao.parcelas_futuras_max = 'ilimitado'
        Operacao.parcelas_futuras = list()

class DetalheOperacao:
    def __init__(self):
        DetalheOperacao.nome_reduzido = 'DetOpr'
        DetalheOperacao.atributos = dict()



root = dict()

root['EnvioHistoricoCredito'] = dict()
root['EnvioHistoricoCredito']['nome_reduzido'] = 'EnvoHstCrd'
root['EnvioHistoricoCredito']['limitacao_numerica'] = dict()
root['EnvioHistoricoCredito']['limitacao_numerica']['min'] = 1
root['EnvioHistoricoCredito']['limitacao_numerica']['max'] = 1

root['EnvioHistoricoCredito']['Clientes'] = dict()
root['EnvioHistoricoCredito']['Clientes']['limitacao_numerica'] = dict()
root['EnvioHistoricoCredito']['Clientes']['limitacao_numerica']['min'] = 0
root['EnvioHistoricoCredito']['Clientes']['limitacao_numerica']['max'] = 'ilimitado'
root['EnvioHistoricoCredito']['Clientes']['lista_clientes'] = list()
root['EnvioHistoricoCredito']['Clientes']['lista_clientes']
