import PySimpleGUI as sg
lista = [
    [sg.Text('PAÍS 1')],
    [sg.Button('AUSTRÁLIA'), sg.Button('LIMPAR')],
    [sg.Radio('AUSTRÁLIA', 'radio1')],
    [sg.Text(''), sg.Text(key='resultado')]
]
janela_lista = sg.Window('LISTA', layout=lista)
while True:
    evento, valor = janela_lista.read()
    if evento == sg.WIN_CLOSED:
        break
    elif evento == 'AUSTRÁLIA':
        resultado = janela_lista['resultado'].update('AUSTRÁLIA')
    elif evento == 'LIMPAR':
        resultado = janela_lista['resultado'].update('')