# importa a lib para obter as tabelas da Wikipedia
from  lib.scrapy_table import Scrapy_Table

# Variavel com o link da tabela
url="https://pt.wikipedia.org/wiki/Lista_de_senadores_do_Brasil_da_56.%C2%AA_legislatura"
url_jato="https://pt.wikipedia.org/wiki/Lista_de_pessoas_envolvidas_na_Opera%C3%A7%C3%A3o_Lava_Jato"

# Inicia a class para obter a tabela
site_senadores = Scrapy_Table(url)
site_jato       = Scrapy_Table(url_jato)

# Pegando as tabelas
senadores      = tuple(site_senadores.get_tables(3))
lista_lava_jato = tuple(site_jato.get_tables(1))

# Criar uma tuple com os nomes dos investigados
lista_investigados = ()
for investigados in  lista_lava_jato[1:]:
    lista_investigados = lista_investigados + (investigados[0],)

# pesquisar nome por nome de vereador na lista de investigado
for senador in senadores[1:]:
    # Verifica se o nome do vereador esta na lista de investigados
    if senador[0] in lista_investigados:
       print(senador)
