from bs4 import BeautifulSoup
import requests
import pandas as pd

link = 'https://globoplay.globo.com/garota-do-momento/t/nHk7j9gJpP/'

requisicao = requests.get(link)
##print(requisicao)

site = BeautifulSoup(requisicao.text, 'html.parser')

##print(site.prettify())

titulos = site.find_all('h3', class_='title-episode__title')
descricoes = site.find_all('p', class_='title-episode__description')

lista_titulos = [titulo.text.strip() for titulo in titulos]
lista_descricoes = [descricao.text.strip() for descricao in descricoes]

if len(lista_titulos) > len(lista_descricoes):
    lista_descricoes.extend(['Descrição não disponível'] * (len(lista_titulos) - len(lista_descricoes)))
elif len(lista_descricoes) > len(lista_titulos):
    lista_titulos.extend(['Título não disponível'] * (len(lista_descricoes) - len(lista_titulos)))

tabela = pd.DataFrame({
    'Título': lista_titulos,
    'Descrição': lista_descricoes
})

print(tabela)

tabela.to_excel('episodios.xlsx', index=False)
