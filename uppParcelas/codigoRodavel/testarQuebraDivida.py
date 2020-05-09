from quebraDivida import quebraDivida
import json
from pprint import pprint

arquivo = open('entradaTesteQuebrarDivida.json','r')
entrada = json.load(arquivo)

contrato = entrada['contrato']
dataDeVisualizacao = entrada['dataDeVisualizacao']

pprint(quebraDivida(contrato, dataDeVisualizacao))
