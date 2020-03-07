import requests
import csv
from bs4 import BeautifulSoup

# Quantidade de comentarios principais e de respostas que os alunos fizeram

def remove_html_tags(text):
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


page = requests.get('https://econofin-bsi.blogspot.com/2019/11/t10a1-analise-de-mercado-de-acoes.html')

soup = BeautifulSoup(page.text, 'html.parser')

for div in soup.find_all("div", {'class': 'avatar-image-container'}):
    div.decompose()

for div in soup.find_all("p", {'class': 'comment-content'}):
    div.decompose()

for div in soup.find_all("span", {'class': 'comment-actions secondary-text'}):
    div.decompose()

for div in soup.find_all("span", {'class': 'icon user'}):
    div.decompose()

for div in soup.find_all("div", {'class': 'comment-replies'}):
    div.decompose()

for div in soup.find_all("span", {'class': 'datetime secondary-text'}):
    div.decompose()

for div in soup.find_all("div", {'class': 'comment-replybox-single'}):
    div.decompose()

raw_content = list()
lista_alunos = soup.find(class_='comment-thread toplevel-thread')
items_lista_alunos = lista_alunos.find_all('ol')

for alunos in items_lista_alunos:
    raw_content.append(remove_html_tags(str(alunos.contents)))

#Foramata o conteudo obtido acima
filtered_content = raw_content[0]
filtered_content = filtered_content.replace('[', '').replace(']', '')
filtered_content = filtered_content.split(',')
count = 0
for aluno in filtered_content:
    filtered_content[count] = filtered_content[count].lstrip()
    count += 1

# Retornando dicionario de alunos que tem comentarios princiais
dictAlunosIds = dict.fromkeys(filtered_content, 0)

for aluno in filtered_content:
    if aluno in dictAlunosIds:
        dictAlunosIds[aluno] += 1

# Escreve no CSV os alunos e a quantidade de comentarios principais que tiveram
with open('qtd_comentarios_principais.csv', 'w') as f:
    for key in dictAlunosIds.keys():
        f.write("%s, %s\n" % (key, dictAlunosIds[key]))

with open('qtd_interacoes_alunos.csv', 'r') as lista_alunos:
    reader = csv.reader(lista_alunos)
    dict_qtd_interacoes = {rows[0]: int(rows[1]) for rows in reader}

# print(dictAlunosIds)
# print(dict_qtd_interacoes)

# Torna a qtd de interadcoes na qtd de respostas subtraindo os principais do total de interacoes
for aluno in dict_qtd_interacoes:
    if aluno in dictAlunosIds.keys():
        dict_qtd_interacoes[aluno] = dict_qtd_interacoes[aluno] - dictAlunosIds[aluno]

print(dict_qtd_interacoes)

#Escreve a quantidade de vezes que o aluno comentou uma resposta
with open('qtd_respostas.csv', 'w') as f:
    for key in dict_qtd_interacoes.keys():
        f.write("%s, %s\n" % (key, dict_qtd_interacoes[key]))


