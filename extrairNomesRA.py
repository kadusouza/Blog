import requests
import csv
import re
import TextUtil
import BeautifulSoupUtil
from bs4 import BeautifulSoup


with open('../topico.csv', 'r') as arquivo_topico:
    reader = csv.reader(arquivo_topico)
    for linha in reader:
        topico = linha[0]

page = requests.get(topico)

soup = BeautifulSoup(page.text, 'html.parser')

# Remove tags desnecessarias
BeautifulSoupUtil.decomposeSpanDatetimeSecondaryText(soup)
BeautifulSoupUtil.decomposeSpanCommentactionsSecondaryText(soup)
BeautifulSoupUtil.decomposeSpanThreadToggleThreadExpanded(soup)
BeautifulSoupUtil.decomposeDivContinue(soup)
BeautifulSoupUtil.decomposePCommentFooter(soup)

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

ra = []
count = 0
for comment in comentarios:
    ra.append(re.findall(r'(\d{6})', comentarios[count]))
    count += 1

dictDeAlunosRA = {i: [] for i in nomes}

count = 0
for nome in nomes:
    if len(dictDeAlunosRA.get(nomes[count])) == 0:
        dictDeAlunosRA[nome].append(ra[count])
    elif dictDeAlunosRA.get(nome)[0] != ra[count]:
        dictDeAlunosRA[nome].append(ra[count])
    count += 1

# Escreve no CSV os alunos e a quantidade de interacoes que tiveram
with open('aluno_ra.csv', 'w') as f:
    for key in dictDeAlunosRA.keys():
        f.write("%s, %s\n" % (key, dictDeAlunosRA[key]))

print(dictDeAlunosRA)



