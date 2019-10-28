import xmlschema
from time import sleep

path_xml = r'C:\Users\jean_\Google Drive\3-Operacional\Cadastro Positivo Boa Vista\Exemplos XML_XSD\XML_005_completo.xml'
path_xsd = r'C:\Users\jean_\Google Drive\3-Operacional\Cadastro Positivo Boa Vista\Exemplos XML_XSD\XSD_005.xsd'

schema = xmlschema.XMLSchema(path_xsd)
root = schema.root[0]

print(schema)

print(root.attrib)

# print(schema.is_valid(path_xml))

a = input("Press Enter to end...")

print(a)

b = input("Press Enter to end...")

# print('types')
# print(schema.types)
# print('elements')
# print(schema.elements)
# print('attributes')
# print(schema.attributes)
