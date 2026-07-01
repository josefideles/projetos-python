import PySimpleGUI as sg
layout = [
    [sg.Text('Selecione os botões e veja o resultado:')],
    [sg.Combo(['um', 'dois', 'tres']), sg.Button('OK')],
    [sg.Button('Botao1'), sg.Button('Botao2'), sg.Button('Botao3')],
    [sg.Checkbox('My first CheckBox', default=True), sg.Checkbox('My second CheckBox')],
    [sg.Radio('My first Radio', 'Radio1', default=True), sg.Radio('My second Radio', 'Radio2')],
    [sg.Text('', key='resposta')]
]
window = sg.Window('Menu Botões', layout=layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'OK':
        window['resposta'].update('Your choose was "combo um"')