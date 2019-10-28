import csv
import xml.etree.ElementTree as ET
from xml.dom import minidom
from lxml import etree

def importar_dicionario():
    dicionario_arquivo = open(r'C:\Users\jean_\Documents\GitHub\Up.p\Operacional\cadastro_positivo\auxiliares\dict_bvs.csv')
    dicionario_csv = csv.reader(dicionario_arquivo, delimiter=';')
    dicionario = dict()
    for row in dicionario_csv:
        dicionario[row[0]] = row[1]

    return dicionario

dict_bvs = importar_dicionario()

enviohistoricocredito = ET.Element('EnvioHistoricoCredito', CnpjFonte='12345678000195', CnpjGestorBD='98765432000198', ComandoRemessa='I', NumeroRemessa='1', SequencialRemessa='1', DataRemessa='05082017', DataReferenciaBaseInterna='04082017', NumeroRemessaRelacao='123', FormatoRemessa='I')
cliente = ET.SubElement(enviohistoricocredito, 'Cliente', TipCliente='1', IdfcCliente='12345678909', NmCliente='JOAO SILVA', NaturezaRelacao='2', CmdoCliente='A', CodigoOcorrencia='0')
operacao = ET.SubElement(cliente, 'Operacao', NumeroUnico='20170000000001', DataContratacao='01032017', Modalidade='A01', DataApuracao='04082017', CnpjContratacao='12345678000195' )
detalheoperacao = ET.SubElement(operacao, 'DetOperacao', IndicadorPreFixado='S', DataVencimentoUltimaParcela='01042018', ValorContratadoFuturo='1500000', QuantidadeParcelas='15')
parcelaanterior = ET.SubElement(detalheoperacao, 'ParcelaAnterior', DtVnctParcelaAnterior='01042017', PercParcelaAnterior='M', VlParcelaAnterior='100000')
pagamentoparcelaanterior = ET.SubElement(parcelaanterior, 'PgtoParcelaAnterior', DtPgtoParcelaAnterior='01042017', VlPgtoParcelaAnterior='100000')



tree = ET.ElementTree(enviohistoricocredito)
