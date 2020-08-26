import gspread
import csv
import CreateGoogleService
import time
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('../client_secret.json', scope)
client = gspread.authorize(creds)
gsheet_id = '1XLdii1HxXz96jfheIZh4iTCxvNWHvWJeAHMOgxt04P0'



alunos = []
registro_academico = []
with open('../aluno_ra.csv', 'r') as lista_alunos:
    reader = csv.reader(lista_alunos)
    for linha in reader:
        alunos.append(linha[0])
        registro_academico.append(linha[1].replace('[', '').replace(']', '').replace('\'', ''))

count = 0
with open('../aluno_ra.csv', 'w') as f:
    for aluno in alunos:
        f.write("%s, %s\n" % (aluno, registro_academico[count]))
        print(aluno)
        print(registro_academico[count])
        count += 1

# Read CSV file contents
content = open('../aluno_ra.csv', 'r').read()

client.import_csv(gsheet_id, content)

CLIENT_SECRET_FILE = '../api_secret.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

service = CreateGoogleService.Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)

spreadsheets = service.spreadsheets()

def add_sheets(gsheet_id, sheet_name):
    try:
        request_body = {
            'requests': [{
                'addSheet': {
                    'properties': {
                        'title': sheet_name,
                        'tabColor': {
                            'red': 0.44,
                            'green': 0.99,
                            'blue': 0.50
                        }
                    }
                }
            }]
        }

        response = spreadsheets.batchUpdate(
            spreadsheetId=gsheet_id,
            body=request_body
        ).execute()

        return response
    except Exception as e:
        print(e)

xSheets = ['Comentarios', 'Palavras', 'Conceitos']
for name in xSheets:
    print(add_sheets(gsheet_id, name))



arquivos = ['../dados_agregados.csv']
aluno = []
qtd = []
row = []
row_index = 1
sheet_index = 1
for arquivo in arquivos:
    row_index = 1
    sheets = client.open("dados").get_worksheet(sheet_index)
    with open(arquivo, 'r') as lista_alunos:
        reader = csv.reader(lista_alunos)
        for linha in reader:
            row.append(linha[0])
            row.append(linha[1])
            row.append(linha[2])
            row.append(linha[3])
            sheets.insert_row(row, row_index)
            row = []
            row_index += 1
    sheet_index += 1
    print("Sleeping for 100 sec")
    time.sleep(100)

with open('../qtd_interacoes_alunos.csv', 'r') as lista_alunos:
    reader = csv.reader(lista_alunos)
    dict_qtd_interacoes = {}
    index = 1
    for rows in reader:
        dict_qtd_interacoes[index] = int(rows[1])
        index += 1

arquivoPalavras = ['../qtd_palavras.csv']
for arquivo in arquivoPalavras:
    row_index = 1
    sheets = client.open("dados").get_worksheet(2)
    with open(arquivo, 'r') as lista_alunos:
        reader = csv.reader(lista_alunos)
        for linha in reader:
            linhaIndex = 0
            total = dict_qtd_interacoes[row_index] + 2
            while linhaIndex < total:
                row.append(linha[linhaIndex])
                linhaIndex += 1
            sheets.insert_row(row, row_index)
            row = []
            row_index += 1
    sheet_index += 1
    print("Sleeping for 100 sec")
    time.sleep(100)
