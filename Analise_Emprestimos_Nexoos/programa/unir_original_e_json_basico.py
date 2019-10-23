from pprint import pprint
import csv
import json

entrada_json = open(r'JSONs\completo.json', 'r', encoding='utf-8')
entrada = open(r'CSVs\saida_tabelas_completo_original.csv', 'r')
saida = open(r'CSVs\tabela_completa.csv', 'w', newline='', encoding='utf-8')

entrada_csv = csv.reader(entrada, delimiter = ';')
saida_csv = csv.writer(saida, delimiter = ';')
entrada_arvore = json.load(entrada_json)

i = 0
for row in entrada_csv:
    linha_saida = list()

    if i != 0:
        if i != 1:
            del entrada_arvore[i-1]['valor_possivel_de_ser_investido']
            del entrada_arvore[i-1]['list_investidores']
        linha_saida = row + list(entrada_arvore[i-1].values())
    else:
        del entrada_arvore[i]['valor_possivel_de_ser_investido']
        del entrada_arvore[i]['list_investidores']
        linha_saida = row + list(entrada_arvore[i].keys())

    saida_csv.writerow(linha_saida)
    i = i + 1

saida.close
