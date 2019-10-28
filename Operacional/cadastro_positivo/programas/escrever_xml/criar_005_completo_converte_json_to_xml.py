import csv
from pprint import pprint
import json
import dict2xml

def importar_dicionario():
    dicionario_arquivo = open(r'C:\Users\jean_\Documents\GitHub\Up.p\Operacional\cadastro_positivo\auxiliares\dict_bvs.csv')
    dicionario_csv = csv.reader(dicionario_arquivo, delimiter=';')
    dicionario = dict()
    for row in dicionario_csv:
        dicionario[row[0]] = row[1]

    return dicionario

dict_bvs = importar_dicionario()

root = dict()
root['EnvioHistoricoCredito'] = dict()
root['EnvioHistoricoCredito']['CnpjFonte'] = '34046974000128'
root['EnvioHistoricoCredito']['CnpjGestorBD'] = '11725176000127'
root['EnvioHistoricoCredito']['ComandoRemessa'] = 'I'
root['EnvioHistoricoCredito']['NumeroRemessa'] = 1
root['EnvioHistoricoCredito']['SequencialRemessa'] = 1
root['EnvioHistoricoCredito']['DataRemessa'] = '25102019'
root['EnvioHistoricoCredito']['DataReferenciaBaseInterna'] = '25102019'
root['EnvioHistoricoCredito']['FormatoRemessa'] = 'C'
root['EnvioHistoricoCredito']['Cliente'] = list()
root['EnvioHistoricoCredito']['Cliente'].append(dict())
root['EnvioHistoricoCredito']['Cliente'][-1]['TipCliente'] = 2
root['EnvioHistoricoCredito']['Cliente'][-1]['IdfcCliente'] = '03712945000124'
root['EnvioHistoricoCredito']['Cliente'][-1]['NmCliente'] = 'Jrsantos serviços médicos'
root['EnvioHistoricoCredito']['Cliente'][-1]['NaturezaRelacao'] = 2
root['EnvioHistoricoCredito']['Cliente'][-1]['CodigoOcorrencia'] = 0

saida = open('teste_005_de_um_dict.xml', 'w', newline='')

xml_str = dict2xml.dict2xml(root, saida)

for line in xml_str:
    saida.write(line)

saida.close
