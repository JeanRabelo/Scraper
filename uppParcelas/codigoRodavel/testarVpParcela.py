import vpParcela
import json

arquivo = open('entradaTesteVpParcela.json','r')
entrada = json.load(arquivo)

contrato = entrada['contrato']
parcela = entrada['parcela']
dataDeVisualizacao = entrada['dataDeVisualizacao']

print(vpParcela.valorPresenteParcela(contrato, parcela, dataDeVisualizacao))
