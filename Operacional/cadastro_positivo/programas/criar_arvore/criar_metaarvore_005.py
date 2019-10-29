# import json


class Historico:

    def __init__(self):

        class Cliente:
            class Operacao:
                class DetalheOperacao:
                    def __init__(self):
                        self.nome_reduzido = 'DetOpr'
                        self.atributos = {'InPreFix' : '',
                        'DtVnctUltPcl' : '',
                        'VlCtrdFut' : '',
                        'QtPcl' : '',
                        'NrPlstCrt' : '',
                        'SdoDvdr' : '',
                        'DtVnctOpr' : '',
                        'NrGr' : '',
                        'CdCt' : '',
                        'SeqCt' : '',
                        'SitCt' : '',
                        'VlObgc' : '',
                        'DtVnctUltPclCsr' : '',
                        'QtPclCtCsr' : '',
                        'SdoDvdrCtCsr' : '',
                        'DtContCtCsr' : ''}

                class ParcelaAnterior:
                    class PagamentoParcelaAnterior:
                        def __init__(self):
                            self.nome_reduzido = 'PgtoPclAnt'
                            self.atributos = {'DtPgtoPclAnt' : '',
                            'VlPgtoPclAnt' : ''}

                    def __init__(self):
                        self.nome_reduzido = 'PclAnt'
                        self.atributos = {'DtVnctPclAnt' : '',
                        'PercPclAnt' : '',
                        'VlPclAnt' : '',
                        'CmdoPclAnt' : ''}

                        self.pagamentos_parcela_anterior_min = 0
                        self.pagamentos_parcela_anterior_max = 'ilimitado'
                        self.pagamentos_parcela_anterior = list()

                class PagamentoAvulso:
                    def __init__(self):
                        self.nome_reduzido = 'PgtoAvls'
                        self.atributos = {'DtPgtoAvls' : '',
                        'VlPgtoAvls' : '',
                        'TipPgtoAvls' : '',
                        'CmdoPgtoAvls' : ''}

                def __init__(self):
                    self.nome_reduzido = 'Opr'
                    self.atributos = {'NrUnco' : '',
                    'PrfAg' : '',
                    'NrCtr' : '',
                    'DtCtrc' : '',
                    'CdMdld' : '',
                    'DtAprc' : '',
                    'CnpjCtrc' : '',
                    'CmdoOpr' : '',
                    'IdfcCliCtrt' : '',
                    'TipRst' : ''}

                    self.parcelas_anteriores_min = 0
                    self.parcelas_anteriores_max = 'ilimitado'

                    self.pagamentos_avulsos_min = 0
                    self.pagamentos_avulsos_max = 'ilimitado'

                    self.parcelas_futuras_min = 0
                    self.parcelas_futuras_max = 'ilimitado'

            def __init__(self):
                self.nome_reduzido = 'Cli'
                self.atributos = {'TipCli' : '',
                'IdfcCli' : '',
                'NmCli' : '',
                'NtzRlc' : '',
                'CdOcr' : '',
                'CmdoCli' : ''}

                self.operacoes_min = 0
                self.operacoes_max = 'ilimitado'


        self.nome_reduzido = 'EnvoHstCrd'
        self.atributos = {'CnpjIf' : '',
        'CnpjGbd' : '',
        'CmdoRms' : '',
        'NrRms' : '',
        'SeqlRms' : '',
        'DtRms' : '',
        'DtRefBaseItno' : '',
        'NrRmsRlc' : '',
        'FmtRms' : ''}

        self.clientes_min = 0
        self.clientes_max = 'ilimitado'
        self.clientes = Cliente


historico = Historico

print(historico().atributos)
