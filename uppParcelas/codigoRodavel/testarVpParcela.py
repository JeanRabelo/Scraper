from vpParcela import valorPresenteParcela
import json
from pprint import pprint

arquivo = open('entradaTesteVpParcela.json','r')
entrada = json.load(arquivo)

contrato = entrada['contrato']
parcela = entrada['parcela']
dataDeVisualizacao = entrada['dataDeVisualizacao']

pprint(valorPresenteParcela(contrato, parcela, dataDeVisualizacao))
