import requests
import re
from bs4 import BeautifulSoup

def remove_html_tags(text):
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

page = requests.get('https://econofin-bsi.blogspot.com/2019/09/o-proposito-deste-topico-e-discutir.html')

soup = BeautifulSoup(page.text, 'html.parser')

for div in soup.find_all("div", {'class':'avatar-image-container'}):
    div.decompose()

#for div in soup.find_all("div", {'class':'comment-block'}):
    #div.decompose()

for div in soup.find_all("p", {'class':'comment-content'}):
    div.decompose()

for div in soup.find_all("span", {'class':'comment-actions secondary-text'}):
    div.decompose()

for div in soup.find_all("span", {'class':'icon user'}):
    div.decompose()

for div in soup.find_all("div", {'class':'comment-replies'}):
    div.decompose()

for div in soup.find_all("span", {'class':'datetime secondary-text'}):
    div.decompose()

for div in soup.find_all("div", {'class':'comment-replybox-single'}):
    div.decompose()

raw_content = list()
lista_ids = list()
lista_alunos = soup.find(class_='comment-thread toplevel-thread')
items_lista_alunos = lista_alunos.find_all('ol')
items_lista_ids = lista_alunos.find_all('li')

for alunos in items_lista_alunos:
    raw_content.append(remove_html_tags(str(alunos.contents)))

for alunos in items_lista_ids:
    lista_ids.append(str(alunos.get('id')))


print(lista_ids)
raw_content = raw_content[0].replace()
raw_content = raw_content[0].split(',')

print(raw_content)
#print(filred_content)

dictAlunosIds = dict(zip(raw_content, lista_ids))
print(dictAlunosIds)


