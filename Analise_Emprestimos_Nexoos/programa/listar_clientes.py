import csv
import json

entrada_json = open(r'JSONs\completo.json', 'r', encoding='utf-8')
saida = open(r'CSVs\tabela_clientes.csv', 'w', newline='', encoding='utf-8')

dados = json.load(entrada_json)
saida_csv = csv.writer(saida, delimiter=';')

saida_csv.writerow(list(dados[0]['list_investidores'][0].keys())+['razao_social', 'motivo', 'prazo', 'juros', 'capital_social', 'rating', 'valor_do_emprestimo'])

for emprestimo in dados:
    for investidor in emprestimo['list_investidores']:
        saida_csv.writerow(list(investidor.values()) + [emprestimo['razao_social'], emprestimo['motivo'], emprestimo['prazo'], emprestimo['juros'], emprestimo['capital_social'], emprestimo['rating'], emprestimo['valor_do_emprestimo ']])


saida.close
