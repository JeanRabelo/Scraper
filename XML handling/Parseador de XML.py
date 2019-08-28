from importar_dados import read_dict_boavista
from importar_dados import read_file

dict_bvs = read_dict_boavista()
root = read_file()

def print_conveniente(str_nivel, elem, indentacao, j, n='root'):
    print(indentacao*'\t', end = '')
    print('-'+str_nivel+'-')
    print(indentacao*'\t', end = '')
    dict_original = elem.attrib
    dict_novo = dict()
    for oldkey in dict_original.keys():
        dict_novo[dict_bvs[oldkey]] = dict_original[oldkey]
    print(dict_novo)
    print(indentacao*'\t', end = '')
    print(str(j) + r'/' + str(n) + ' - \\' + str(len(elem)) + r'/')

def percorrer_arvore(root, int_nivel=0, j_n=1, n=1):
    print_conveniente(int_nivel*'sub_' + 'element', root, int_nivel, j_n, n)
    n = len(root)
    if n > 0:
        j_n = 1
        for elem in root:
            percorrer_arvore(elem, int_nivel + 1, j_n, n)
            j_n = j_n + 1

percorrer_arvore(root)
