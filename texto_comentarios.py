import requests
import csv
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

# Lista com os nomes sem repeticao
unique_names = []
with open('../lista_alunos.csv', 'r') as lista_alunos:
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


for aluno in dictDeAlunos:
    total = sum(dictDeAlunos[aluno])
    num_elementos = len(dictDeAlunos[aluno])
    media = total / num_elementos
    dictDeAlunos[aluno].append(media)

print(dictDeAlunos)

# Escreve no CSV os alunos, a quantidade de palavras por comentario e por ultimo a média de palavras usadas
with open('../qtd_palavras.csv', 'w') as f:
    for key in dictDeAlunos.keys():
        i = 0
        tamanhoReal = len(dictDeAlunos[key]) - 1
        f.write("%s, " % key)
        while i <= tamanhoReal:
            print(tamanhoReal)
            print(i)
            if i == tamanhoReal:
                f.write("%.2f" % dictDeAlunos[key][i])
                f.write("\n")
            else:
                f.write("%.0f, " % dictDeAlunos[key][i])
            i += 1
