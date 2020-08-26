import csv

# Botar comentarios, respostas e total cada um em um array
# Escrever isso em um arquivo para ser lido se jogado no google sheets
alunos = []
with open('../qtd_interacoes_alunos.csv', 'r') as lista_alunos:
    reader = csv.reader(lista_alunos)
    dict_qtd_interacoes = {}
    for rows in reader:
        dict_qtd_interacoes[rows[0]] = int(rows[1])
        alunos.append(rows[0])

with open('../qtd_respostas.csv', 'r') as lista_alunos:
    reader = csv.reader(lista_alunos)
    dict_respostas = {}
    for rows in reader:
        dict_respostas[rows[0]] = int(rows[1])

with open('../qtd_comentarios_principais.csv', 'r') as lista_alunos:
    reader = csv.reader(lista_alunos)
    dict_qtd_comentarios_principais = {}
    for rows in reader:
        dict_qtd_comentarios_principais[rows[0]] = int(rows[1])

dictAgregatedData = {k: [] for k in alunos}
for aluno in dict_qtd_interacoes:
    if aluno in dict_qtd_comentarios_principais:
        dictAgregatedData[aluno].append(dict_qtd_comentarios_principais[aluno])
    else:
        dictAgregatedData[aluno].append(0)
    if aluno in dictAgregatedData:
        dictAgregatedData[aluno].append(dict_respostas[aluno])
        dictAgregatedData[aluno].append(dict_qtd_interacoes[aluno])

print(dictAgregatedData)
# Escreve no CSV os alunos, a quantidade de palavras por comentario e por ultimo a média de palavras usadas
with open('../dados_agregados.csv', 'w') as f:
    for key in dictAgregatedData.keys():
        f.write("%s, %s, %s, %s\n" % (key, dictAgregatedData[key][0],
                                      dictAgregatedData[key][1],
                                      dictAgregatedData[key][2]))
