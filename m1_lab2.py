# importa a lib para obter as tabelas da Wikipedia
from  lib.scrapy_table import Scrapy_Table

# Variavel com o link da tabela
url="https://pt.wikipedia.org/wiki/C%C3%A2mara_Municipal_de_S%C3%A3o_Paulo"

# Inicia a class para obter a tabela
site_connect = Scrapy_Table(url)

# Pegando a tabela 5 (Vereadores em exercicio)
tables = site_connect.get_tables(5)
  
# Cria um set porque nao queremos partidos repetidos
partidos = set() 

# Listando a tabela
for linha in tables[1:]:
    if linha[1].startswith('P'):
    # Obtendo o nome. Esta na primeira posicao da lista
      partidos.add(linha[1])

# Imprimindo os partidos
for partido in partidos:
    print(partido)
