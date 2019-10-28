import xml.etree.ElementTree as ET
import xmlschema
import csv

def importar_dicionario():
    dicionario_arquivo = open(r'C:\Users\jean_\Documents\GitHub\Up.p\Operacional\cadastro_positivo\auxiliares\dict_bvs.csv')
    dicionario_csv = csv.reader(dicionario_arquivo, delimiter=';')
    dicionario = dict()
    dicionario_reverso = dict()
    for row in dicionario_csv:
        dicionario[row[0]] = row[1]
        dicionario_reverso[row[1]] = row[0]

    return [dicionario, dicionario_reverso]

[dict_bvs, dict_bvs_reverso]  = [importar_dicionario()[0], importar_dicionario()[1]]

schema = xmlschema.XMLSchema(r'C:\Users\jean_\Google Drive\3-Operacional\Cadastro Positivo Boa Vista\Exemplos XML_XSD\XSD_005.xsd')
root = schema.root

enviohistoricocredito = ET.Element('EnvioHistoricoCredito', CnpjFonte='12345678000195', CnpjGestorBD='98765432000198', ComandoRemessa='I', NumeroRemessa='1', SequencialRemessa='1', DataRemessa='05082017', DataReferenciaBaseInterna='04082017', NumeroRemessaRelacao='123', FormatoRemessa='I')

print(schema)
print(root)

b = input("Press Enter to end...")





# Atributos:
# elementFormDefault
# version
# name
# maxOccurs
# minOccurs
# type
# use
# base
