import pandas as pd
from pprint import pprint

def read_dict_boavista():
    str_path_dicionario_bvs = r'C:\Users\jean_\Documents\GitHub\Up.p\XML handling\Dicionario_termos_boavista.csv'
    df = pd.read_csv(str_path_dicionario_bvs, sep=';')
    dict_bvs = df.set_index('Tag ou Atributo')['Nome Completo'].to_dict()

    return dict_bvs

# aaa = read_dict_boavista()

# pprint(type(aaa.keys()))

# for oldkey in aaa.keys():
#     print(type(oldkey))
