# importa a lib para obter as tabelas da Wikipedia
from  lib.scrapy_table import Scrapy_Table

# Variavel com o link da tabela
url="https://pt.wikipedia.org/wiki/C%C3%A2mara_Municipal_de_S%C3%A3o_Paulo"

# Inicia a class para obter a tabela
site_connect = Scrapy_Table(url)

# Pegando a tabela 5 (Vereadores em exercicio)
tables = site_connect.get_tables(5)
  
# Listando o conteudo da tabela

#Variavél para somatória de votos
total = 0 

for linha in tables[1:]:

    # Obtendo o numo de votos do cantidato
    voto= linha[2]
          
    # No campo do voto, pode ter alguma letras que pode dar erro na hora de converter para float
    # Ex: 24.461 (não eleito)
    # Para resolver isso usamos o split para quebrar a string voto quando encontrar espaco em branco.
    # Como resultado vai ser criado uma lista com 2 posicao, sendo sempre a primeira posicao o número de votos
   
    num = voto.split(" ")

    print(linha[0] + ' = ' + num[0] + ' votos.')

    # somando com o total  com o num[0] que tem os votos
    total = total + float(num[0])

# Imprimindo o total de votos
print(total)
