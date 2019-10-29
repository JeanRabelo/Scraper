import csv
import xml.etree.ElementTree as ET

def importar_dicionario():
    dicionario_arquivo = open(r'C:\Users\jean_\Documents\GitHub\Up.p\Operacional\cadastro_positivo\auxiliares\dict_bvs.csv')
    dicionario_csv = csv.reader(dicionario_arquivo, delimiter=';')
    dicionario = dict()
    dicionario_reverso = dict()
    for row in dicionario_csv:
        dicionario[row[0]] = row[1]
        dicionario_reverso[row[1]] = row[0]


    return [dicionario, dicionario_reverso]

[dict_bvs, dict_bvs_reverso] = [importar_dicionario()[0], importar_dicionario()[1]]

def preencher_historico():
    CnpjFonte =  str(input('Cnpj da Fonte de dados\n')).replace(r'-', '').replace(r'/', '').replace(r'.', '')
    CnpjGBD = str(input('Cnpj do Gestor de Banco de dados\n')).replace(r'-', '').replace(r'/', '').replace(r'.', '')
    ComandoRemessa = str(input('I: inclusão\nE: exclusão\n')).upper()
    NumeroRemessa = str(int(input('Número da remessa\n')))
    SequencialRemessa = str(int(input('Sequencial da remessa\n')))
    DataRemessa = str(input('Data da remessa\n'))
    DataReferenciaBaseInterna = str(input('Data de consolidação da base interna\n'))
    NumeroRemessaRelacao = str(int(input('Numero de remessa da relacao\n')))
    FormatoRemessa = str(input('C - completo\nI - incremental\n'))

    noh = ET.Element('EnvoHstCrd')

    # CnpjIf = CnpjFonte,
    # CnpjGbd = CnpjGBD,
    # CmdoRms = ComandoRemessa,
    # NrRms = NumeroRemessa,
    # SeqlRms = SequencialRemessa,
    # DtRms = DataRemessa,
    # DtRefBaseItno = DataReferenciaBaseInterna,
    # NrRmsRlc = NumeroRemessaRelacao,
    # FmtRms = FormatoRemessa)

    noh.set('CnpjIf', CnpjFonte)
    noh.set('CnpjGbd', CnpjGBD)
    noh.set('CmdoRms', ComandoRemessa)
    noh.set('NrRms', NumeroRemessa)
    noh.set('SeqlRms', SequencialRemessa)
    noh.set('DtRms', DataRemessa)
    noh.set('DtRefBaseItno', DataReferenciaBaseInterna)
    noh.set('NrRmsRlc', NumeroRemessaRelacao)
    noh.set('FmtRms', FormatoRemessa)

    return noh

def preencher_cliente(enviohistoricocredito):
    TipoCliente = str(input('\t'+r'1 - PF / 2 - PJ (CNPJ completo) / 3 - PJ (radical de CNPJ)' + '\n\t'))
    IdentificacaoCliente = str(input('\t'+r'CPF/CNPJ' + '\n\t'))
    NomeCliente = str(input('\tNome do cliente\n\t'))
    NaturezaRelacao = str(input('\t'+r'1 - comercial / 2 - creditícia  / 3 - serviços continuados / 4 - consórcio / 5- creditícia e consórcio /  9 - outros' + '\n\t'))
    CodigoOcorrencia = str(input('\tCodigo ocorrencia (seja la o que isso significar)\n\t'))
    ComandoCliente = str(input('\t'+r'I - inclusão / A - alteração / E - exclusão' + '\n\t'))

    noh = ET.SubElement(enviohistoricocredito, 'Cli')
    # return ET.SubElement(enviohistoricocredito, 'Cli',
    # TipCli = TipoCliente,
    # IdfcCli = IdentificacaoCliente,
    # NmCli = NomeCliente,
    # NtzRlc = NaturezaRelacao,
    # CdOcr = CodigoOcorrencia,
    # CmdoCli = ComandoCliente)

    noh.set('TipCli', TipoCliente)
    noh.set('IdfcCli', IdentificacaoCliente)
    noh.set('NmCli', NomeCliente)
    noh.set('NtzRlc', NaturezaRelacao)
    noh.set('CdOcr', CodigoOcorrencia)
    noh.set('CmdoCli', ComandoCliente)

    return noh

sair = False

enviohistoricocredito = preencher_historico()

add_cliente = str(input('\n\tDeseja adicionar um cliente? (y/n)\n\t')).lower()
while add_cliente == 'y':
    cliente = preencher_cliente(enviohistoricocredito)
    add_cliente = str(input('\n\tDeseja adicionar um cliente? (y/n)\n\t')).lower()
    # if add_cliente =='y':


# enviohistoricocredito = ET.Element('EnvioHistoricoCredito', CnpjFonte='12345678000195', CnpjGestorBD='98765432000198', ComandoRemessa='I', NumeroRemessa='1', SequencialRemessa='1', DataRemessa='05082017', DataReferenciaBaseInterna='04082017', NumeroRemessaRelacao='123', FormatoRemessa='I')
# cliente = ET.SubElement(enviohistoricocredito, 'Cliente', TipCliente='1', IdfcCliente='12345678909', NmCliente='JOAO SILVA', NaturezaRelacao='2', CmdoCliente='A', CodigoOcorrencia='0')
# operacao = ET.SubElement(cliente, 'Operacao', NumeroUnico='20170000000001', DataContratacao='01032017', Modalidade='A01', DataApuracao='04082017', CnpjContratacao='12345678000195' )
# detalheoperacao = ET.SubElement(operacao, 'DetOperacao', IndicadorPreFixado='S', DataVencimentoUltimaParcela='01042018', ValorContratadoFuturo='1500000', QuantidadeParcelas='15')
# parcelaanterior = ET.SubElement(operacao, 'ParcelaAnterior', DtVnctParcelaAnterior='01042017', PercParcelaAnterior='M', VlParcelaAnterior='100000')
# pagamentoparcelaanterior = ET.SubElement(parcelaanterior, 'PgtoParcelaAnterior', DtPgtoParcelaAnterior='01042017', VlPgtoParcelaAnterior='100000')

tree = ET.ElementTree(enviohistoricocredito)
tree.write(r'C:\Users\jean_\Documents\GitHub\Up.p\Operacional\cadastro_positivo\teste.xml')
