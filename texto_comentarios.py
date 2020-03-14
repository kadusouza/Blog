import requests
import csv
from bs4 import BeautifulSoup


# Function to convert
def listToString(s):
    # initialize an empty string
    str1 = " "

    # return string
    return str1.join(s)


def remove_html_tags(text):
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


page = requests.get('https://econofin-bsi.blogspot.com/2019/11/t10a1-analise-de-mercado-de-acoes.html')

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
    aluno = remove_html_tags(str(nome.contents))
    aluno = aluno.replace('[', '').replace(']', '').replace('\'', '')
    nomes.append(aluno)

comentarios = []
items_lista_comentarios = lista_conteudo.find_all('p')
for comentario in items_lista_comentarios:
    comentarios.append(listToString(comentario.contents))

# Lista com os nomes sem repeticao
unique_names = []
with open('lista_alunos.csv', 'r') as lista_alunos:
    reader = csv.reader(lista_alunos)
    for linha in reader:
        if ''.join(linha).strip():
            if linha[0] not in unique_names:
                unique_names.append(linha[0])

dictDeAlunos = {i: [] for i in unique_names}

count = 0
# Adiciona a quantidade de palavras de cada interacao
for aluno in nomes:
    value = len(comentarios[count].split())
    dictDeAlunos[nomes[count]].append(value)
    count += 1

print(dictDeAlunos)

for aluno in dictDeAlunos:
    total = sum(dictDeAlunos[aluno])
    num_elementos = len(dictDeAlunos[aluno])
    media = total / num_elementos
    dictDeAlunos[aluno].append(media)

print(dictDeAlunos)

# Escreve no CSV os alunos, a quantidade de palavras por comentario e por ultimo a média de palavras usadas
with open('qtd_palavras.csv', 'w') as f:
    for key in dictDeAlunos.keys():
        f.write("%s, %s\n" % (key, dictDeAlunos[key]))
