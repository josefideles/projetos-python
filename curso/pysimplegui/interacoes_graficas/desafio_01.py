import PySimpleGUI
import math

layout = [
    [PySimpleGUI.Text('1º NÚMERO', size=9), PySimpleGUI.Text('2º NÚMERO', size=9), PySimpleGUI.Text('3º NÚMERO', size=9)],
    [PySimpleGUI.Input(key='numero1', size=10), PySimpleGUI.Input(key='numero2', size=10), PySimpleGUI.Input(key='numero3', size=10)],
    [PySimpleGUI.Text('ESCOLHA A OPERAÇÃO QUE DESEJA REALIZAR:')],
    [PySimpleGUI.Button('SOMAR'), PySimpleGUI.Button('MÉDIA'), PySimpleGUI.Button('CONCATENAR')],
    [PySimpleGUI.Text('O resultado da operação é ='), PySimpleGUI.Text('', key='resultado'), PySimpleGUI.Button('LIMPAR')]
]
janela = PySimpleGUI.Window('CALCULANDO', layout=layout)
while True:
    evento, valor = janela.read()
    if evento == PySimpleGUI.WIN_CLOSED:
        break
    elif evento == 'SOMAR':
        valor1 = float(valor['numero1'])
        valor2 = float(valor['numero2'])
        valor3 = float(valor['numero3'])
        soma = valor1 + valor2 + valor3
        janela['resultado'].update(soma)
    elif evento == 'MÉDIA':
        media1 = float(valor['numero1'])
        media2 = float(valor['numero2'])
        media3 = float(valor['numero3'])
        media = soma / 3
        janela['resultado'].update(media)
    elif evento == 'CONCATENAR':
        soma = valor['numero1']+valor['numero2']+valor['numero3']
        janela['resultado'].update(soma)
    elif evento == 'LIMPAR':
        janela['numero1'].update("")
        janela['numero2'].update("")
        janela['numero3'].update("")