import os
import pandas as pd
import xml.etree.ElementTree as ET


'''
Funcionou aqui para trabalhar diretamente com a conversao de arquivo XML para PANDAS DF, porém precisa remover a Tag de String, nao sei porque....
 vou tentar manipular outro arquivo amanhã pela manhã, para apagar esse elemento, depois salvar o arquivo para então fazer o parse para dataframe.
'''

# Correto com o arquivo alterado manualmente para as chaves
# df = pd.read_xml("xml_test\\files\\ventas.xml")

with open('xml_test\\files\\ventas_jul01.xml', encoding='utf-8', mode='r') as f:
    for line in f:
        xml_openkey = line.replace('&lt;', '<')
        xml_closekey = line.replace('&gt;', '>')
        print(line)


df = pd.read_xml('xml_test\\files\\ventas_jul01.xml') # To be checked later, namespaces={"ns0":"http://wsGenQueryFacade/"}, xpath="//ns0:Table")

print(df.shape)
print(df.head(2))
print(df.columns)

