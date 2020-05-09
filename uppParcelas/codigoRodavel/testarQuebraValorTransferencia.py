from quebraValorTransferencia import quebraTransferencia
import json
from pprint import pprint

arquivo = open('entradaTesteTransferencia.json','r')
entrada = json.load(arquivo)

contrato = entrada['contrato']
dataTransferencia = entrada['dataTransferencia']
valorTransferencia = entrada['valorTransferencia']
parcela = entrada['parcela']

pprint(quebraTransferencia(contrato, dataTransferencia, valorTransferencia, parcela))
