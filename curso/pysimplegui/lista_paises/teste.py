import PySimpleGUI as sg
janela = [
    [sg.T('AUSTRÁLIA'), sg.Text('BRASIL'), sg.Text('ITÁLIA')],
    [sg.B('AUSTRÁLIA1'), sg.Button('BRASIL'), sg.Button('ITÁLIA')], [sg.Text('ESCOLHIDO'), sg.Text(key='resultado')],
    ]
janela_lista = sg.Window('LISTA', layout=janela)
while True:
    evento, valor = janela_lista.read()
    if evento == sg.WIN_CLOSED:
        break
    elif evento == 'AUSTRÁLIA1':
        resultado = janela_lista['resultado'].update('AUSTRÁLIA')
    elif evento == 'LIMPAR':
        resultado = janela_lista['resultado'].update('')