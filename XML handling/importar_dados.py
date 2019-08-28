import xml.etree.cElementTree as ET
import pandas as pd

def read_dict_boavista():
    str_path_dicionario_bvs = r'C:\Users\jean_\Documents\GitHub\Up.p\XML handling\Dicionario_termos_boavista.csv'
    df = pd.read_csv(str_path_dicionario_bvs, sep=';')
    dict_bvs = df.set_index('Tag ou Atributo')['Nome Completo'].to_dict()

    return dict_bvs

def read_file():
    str_file = r"C:\Users\jean_\Google Drive\3-Operacional\Cadastro Positivo Boa Vista\XML_BVXA005_completo_ Modelo.xml"

    tree = ET.parse(str_file)
    root = tree.getroot()
    return root
