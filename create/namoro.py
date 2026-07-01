import PySimpleGUI as sg
layout = [
    [sg.Text('VOCÊ ACEITA NAMORAR COMIGO?'.upper())],
    [sg.Radio('claro, eu aceito!!'.upper(), 'group'), sg.Radio('não!'.upper(), 'group')],
    [sg.T(''), sg.T(key='result')]
]
window = sg.Window('pedido de namoro'.upper(), layout=layout, resizable=True, grab_anywhere=True)
while True:
    event, values = window.read()
    if event == sg. WClosed:
        break
