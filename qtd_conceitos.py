import re
import requests
import csv
import TextUtil
from bs4 import BeautifulSoup


with open('topico.csv', 'r') as arquivo_topico:
    reader = csv.reader(arquivo_topico)
    for linha in reader:
        topico = linha[0]

print(topico)

page = requests.get(topico)

soup = BeautifulSoup(page.text, 'html.parser')

# Remove tags desnecessarias
for div in soup.find_all("span", {'class': 'datetime secondary-text'}):
    div.decompose()

for div in soup.find_all("span", {'class': 'comment-actions secondary-text'}):
    div.decompose()

for div in soup.find_all("span", {'class': 'thread-toggle thread-expanded'}):
    div.decompose()

for div in soup.find_all("div", {'class': 'continue'}):
    div.decompose()

for div in soup.find_all("p", {'class': 'comment-footer'}):
    div.decompose()

remove_loadmore = soup.find("div", {'class': 'loadmore hidden'})
remove_loadmore.decompose()

for objeto_vazio in soup.find_all():
    if len(objeto_vazio.get_text(strip=True)) == 0:
        objeto_vazio.extract()

# Pega todos os nomes dos alunos
nomes = list()
lista_conteudo = soup.find(class_='comments')
items_lista_nome = lista_conteudo.find_all('cite')
for nome in items_lista_nome:
    aluno = TextUtil.remove_html_tags(str(nome.contents))
    aluno = aluno.replace('[', '').replace(']', '').replace('\'', '')
    nomes.append(aluno)

comentarios = []
items_lista_comentarios = lista_conteudo.find_all('p')
for comentario in items_lista_comentarios:
    comentarios.append(TextUtil.listToString(comentario.contents))

# Lista com os nomes sem repeticao
unique_names = []
with open('lista_alunos.csv', 'r') as lista_alunos:
    reader = csv.reader(lista_alunos)
    for linha in reader:
        if ''.join(linha).strip():
            if linha[0] not in unique_names:
                unique_names.append(linha[0])

dictDeAlunos = {i: [] for i in unique_names}

# Cria dicionário de tópico/conceitos tendo como entrada o csv que deve ter duas colunas e número_tópico ; conceito
# Aqui também é assumido que o número máximo de tópicos é de 15, pode ser mudado caso necessário
qtd_de_topicos = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
dictDeConceitos = {k: [] for k in qtd_de_topicos}

with open('Base de Conceitos.csv', mode='r', encoding='utf-8-sig') as infile:
    reader = csv.reader(infile, delimiter=';')
    for rows in reader:
        if rows[0] not in dictDeConceitos:
            dictDeConceitos[rows[0]].append(rows[1])
        if rows[0] in dictDeConceitos:
            dictDeConceitos[rows[0]].append(rows[1])

# print(dictDeConceitos)
# Mostra quais os patterns que foram encotrados na String que por enquanto é a lista chamada de string
count = 0
i = 0
comment_userd_index = 0
for comment in comentarios:
    for key in dictDeConceitos:
        patterns = dictDeConceitos.get(key)
        for pattern in patterns:
            if re.search(pattern, comment):
                dictDeAlunos[nomes[i]].append(key)
    dictDeAlunos[nomes[i]].append('|')
    i += 1

print(dictDeAlunos)

# Escreve no CSV os coneceitos usados por cada aluno separado por |
with open('qtd_conceitos.csv', 'w') as f:
    for key in dictDeAlunos.keys():
        f.write("%s, %s\n" % (key, dictDeAlunos[key]))
