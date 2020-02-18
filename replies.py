import requests
import re
from bs4 import BeautifulSoup

page = requests.get('https://econofin-bsi.blogspot.com/2019/09/o-proposito-deste-topico-e-discutir.html')

soup = BeautifulSoup(page.text, 'html.parser')

for div in soup.find_all("span", {'class':'datetime secondary-text'}):
    div.decompose()

for div in soup.find_all("a", {'class':'comment-reply'}):
    div.decompose()

for div in soup.find_all("span", {'class': 'thread-count'}):
    div.decompose()

for div in soup.find_all("span", {'class': 'comment-actions secondary-text'}):
    div.decompose()

lista_alunos = soup.find(id='c8720477246029385050')
items_lista_alunos = lista_alunos.find_all('a')
qtd_respostas = - 1
for alunos in items_lista_alunos:
    print(alunos.contents)
    qtd_respostas = qtd_respostas + 1

print(qtd_respostas)