import csv

alunos = []
count = 0
with open('lista_alunos.csv', 'r') as lista_alunos:
    reader = csv.reader(lista_alunos)
    for linha in reader:
        if ''.join(linha).strip():
            if linha[0] not in alunos:
                alunos.append(linha[0])

dictDeAlunos = {i: 1 for i in alunos}

with open('lista_alunos.csv', 'r') as lista_alunos:
    reader = csv.reader(lista_alunos)
    for row in reader:
        for linha in reader:
            if ''.join(linha).strip():
                if linha[0] in dictDeAlunos:
                    dictDeAlunos[linha[0]] += 1

print(dictDeAlunos)

# Escreve no CSV os alunos e a quantidade de interacoes que tiveram
with open('qtd_interacoes_alunos.csv', 'w') as f:
    for key in dictDeAlunos.keys():
        f.write("%s: %s\n" % (key, dictDeAlunos[key]))
