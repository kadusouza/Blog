import PySimpleGUI as sg
import csv
import os


def buscarTopico():
    with open('../topico.csv', 'r') as arquivo_topico:
        reader = csv.reader(arquivo_topico)
        for linha in reader:
            topico = linha[0]
    return topico


def atualizarTopico(value):
    with open('../topico.csv', 'w') as arquivo_topico:
        arquivo_topico.write("%s" % value)


def baseDeConceitos(value):
    # read
    data = []
    with open(value, 'r') as f:
        f_csv = csv.reader(f)
        # header = next(f_csv)
        for row in f_csv:
            data.append(row)

    # write
    with open('../Base de Conceitos.csv', 'w+') as f:
        writer = csv.writer(f)
        for i in range(int(len(data))):
            writer.writerow(data[i])


def rodarScripts():
    os.system('python3 exec.py')


class Interface:
    sg.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text('Link Tópico'), sg.InputText(), sg.Button('Atualizar Tópico')],
              [sg.Text(buscarTopico(), key='-TOPICO-')],
              [sg.Text('Base de Conceitos'), sg.InputText(size=(40, 1)), sg.Button('Inserir base de conceitos')],
              [sg.Text('', size=(40, 1) ,key='-BASE-')],
              [sg.Button('Obter Métricas'), sg.Text('', size=(10, 1), key='-STATUS-')],
              [sg.Button('Enviar para o Google Sheets')],
              [sg.Button('Sair')]]

    # Create the Window
    window = sg.Window('Métricas Blog', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Sair'):  # if user closes window or clicks cancel
            break
        if event in (None, 'Atualizar Tópico'):
            atualizarTopico(values[0])
            window['-TOPICO-'].update(buscarTopico())
            window['-STATUS-'].update('')
            window['-BASE-'].update('')
        if event in (None, 'Obter Métricas'):
            rodarScripts()
            window['-STATUS-'].update('Finalizado')
        if event in (None, 'Inserir base de conceitos'):
            baseConceitoFormat = '../' + values[1]
            baseDeConceitos(baseConceitoFormat)
            window['-BASE-'].update('Nova base de conceitos inserida')
            window['-STATUS-'].update('')

    window.close()


interface = Interface()
