# import json


class Historico:
    def __init__(self):
        self.nome_reduzido = 'EnvoHstCrd'
        self.atributos = dict()

        self.clientes_min = 0
        self.clientes_max = 'ilimitado'
        self.clientes = list()

class Cliente:
    def __init__(self):
        self.nome_reduzido = 'Cli'
        self.atributos = dict()

        self.operacoes_min = 0
        self.operacoes_max = 'ilimitado'
        self.operacoes = list()

class Operacao:
    def __init__(self):
        self.nome_reduzido = 'Opr'
        self.atributos = dict()

        self.detalhe_operacoes_min = 0
        self.detalhe_operacoes_max = 1
        self.detalhe_operacoes = dict()

        self.parcelas_anteriores_min = 0
        self.parcelas_anteriores_max = 'ilimitado'
        self.parcelas_anteriores = list()

        self.pagamentos_avulsos_min = 0
        self.pagamentos_avulsos_max = 'ilimitado'
        self.pagamentos_avulsos = list()

        self.parcelas_futuras_min = 0
        self.parcelas_futuras_max = 'ilimitado'
        self.parcelas_futuras = list()

class DetalheOperacao:
    def __init__(self):
        self.nome_reduzido = 'DetOpr'
        self.atributos = dict()

class ParcelaAnterior:
    def __init__(self):
        self.nome_reduzido = 'PclAnt'
        self.atributos = dict()
        self.pagamentos_parcela_anterior_min = 0
        self.pagamentos_parcela_anterior_max = 'ilimitado'
        self.pagamentos_parcela_anterior = list()

class PagamentoParcelaAnterior:
    def __init__(self):
        self.nome_reduzido = 'PgtoPclAnt'
        self.atributos = dict()

class PagamentoAvulso:
    def __init__(self):
        self.nome_reduzido = 'PgtoAvls'
        self.atributos = dict()
