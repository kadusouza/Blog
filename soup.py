import requests
import csv
from bs4 import BeautifulSoup

with open('topico.csv', 'r') as arquivo_topico:
    reader = csv.reader(arquivo_topico)
    for linha in reader:
        topico = linha[0]

page = requests.get(topico)

soup = BeautifulSoup(page.text, 'html.parser')

# Remove tags desnecessarias
for div in soup.find_all("span", {'class':'datetime secondary-text'}):
    div.decompose()

for div in soup.find_all("span", {'class':'comment-actions secondary-text'}):
    div.decompose()

for div in soup.find_all("span", {'class':'thread-toggle thread-expanded'}):
    div.decompose()

for div in soup.find_all("div", {'class':'continue'}):
    div.decompose()

remove_loadmore = soup.find("div", {'class':'loadmore hidden'})
remove_loadmore.decompose()

# Criando arquivo CSV
f = csv.writer(open('lista_alunos.csv', 'w'))

# Limpa os objetos vazios
for objeto_vazio in soup.find_all():
    if len(objeto_vazio.get_text(strip=True)) == 0:
        objeto_vazio.extract()

# Procura todos alunos com login e os conta
lista_alunos = soup.find(class_='comments')
items_lista_alunos = lista_alunos.find_all('a')
count = 0
ocorrencia = 0
for alunos in items_lista_alunos:
    print(alunos.contents)
    count = count + 1
    names = alunos.contents
    f.writerow(names)


# Remove os alunos com login ja contados anteriormente
for div in soup.find_all('a'):
    div.decompose()

# Limpa os objteos vazios
for objeto_vazio in soup.find_all():
    if len(objeto_vazio.get_text(strip=True)) == 0:
        objeto_vazio.extract()

# Procura pelo alunos sem login e os coloca na contagem
# Lista todos os nomes no CSV de forma nao formatada
lista_alunos_sem_login = soup.find(class_='comments')
items_lista_alunos_sem_login = lista_alunos_sem_login.find_all('cite')
for alunos_sem_login in items_lista_alunos_sem_login:
    print(alunos_sem_login.contents)
    count = count + 1
    names = alunos_sem_login.contents
    f.writerow(names)

print(count)




