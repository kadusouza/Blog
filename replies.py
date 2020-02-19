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


# Para testar, esses resultados serao obtidos do interacoes.py
temporary_id_dictionary = {'Enzo Fuji': 'c8720477246029385050', 'João Pedro de Faria': 'c8288796028292114243',
                           'Anônimo': 'c788449666887733230', 'Letícia Wong': 'c3162302219159244268',
                           'Gabriel Antonio': 'c2016595815497055439', 'Unknown': 'c7692978914926222781',
                           'Mayara Silva Alves': 'c8350160932393360596',
                           'Vinicius Hayashida Viana': 'c4253339910553678877',
                           'Gabriel Penna': 'c6601806323768593711'}

temporary_names_list = ["Enzo Fuji", "João Pedro de Faria", "Anônimo", "Letícia Wong", "Gabriel Antonio", "Unknown",
                        "Mayara Silva Alves", "Vinicius Hayashida Viana", "Gabriel Penna"]


qtd_respostas_dict = {}
count = 0
for resposta in temporary_names_list:
    lista_alunos = soup.find(id=temporary_id_dictionary.get(temporary_names_list[count]))
    items_lista_alunos = lista_alunos.find_all('a')
    qtd_respostas = - 1
    for alunos in items_lista_alunos:
        qtd_respostas = qtd_respostas + 1
    qtd_respostas_dict.update({temporary_names_list[count] : qtd_respostas})
    count = count + 1


print(qtd_respostas_dict)


