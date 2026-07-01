import PySimpleGUI as sg
def soma(janela, valor):
    if valor['number_1'] != '' and valor['number_2'] != '' and valor['number_3'] != '':
        number_1 = float(valor['number_1'])
        number_2 = float(valor['number_2'])
        number_3 = float(valor['number_3'])
        janela_calculadora['resultado'].update(f"O seu resultado é: {number_1+number_2+number_3}")
        janela_calculadora['foto'].update(foto_soma, size=(250,160))
def media(janela, valor):
    if valor['number_1'] != '' and valor['number_2'] != '' and valor['number_3'] != '':
        number_1 = float(valor['number_1'])
        number_2 = float(valor['number_2'])
        number_3 = float(valor['number_3'])
        janela_calculadora['resultado'].update(f"O seu resultado é: {(number_1+number_2+number_3)/3}")
        janela_calculadora['foto'].update(foto_media, size=(250,160))
def concatenar(janela, valor):
    if valor['number_1'] != '' and valor['number_2'] != '' and valor['number_3'] != '':
        janela_calculadora['resultado'].update(f"O seu resultado é: {valor['number_1']+valor['number_2']+valor['number_3']}")
        janela_calculadora['foto'].update(foto_concatenar)
def limpar(janela, valor):
    janela_calculadora['number_1'].update('')
    janela_calculadora['number_2'].update('')
    janela_calculadora['number_3'].update('')
    janela_calculadora['foto'].update(foto_gato)
foto_soma = r"C:\Users\ALUNO\PycharmProjects\pythonProject\codigos\goku\pysimplegui\SOMAR.png"
foto_media = r"C:\Users\ALUNO\PycharmProjects\pythonProject\codigos\goku\pysimplegui\media.png"
foto_concatenar = r"C:\Users\ALUNO\PycharmProjects\pythonProject\codigos\goku\pysimplegui\concatenar.png"
foto_gato = r"C:\Users\ALUNO\PycharmProjects\pythonProject\codigos\goku\pysimplegui\gato.png"
calculadora = [
    [sg.Text('NÚMERO 1'), sg.Text('NÚMERO 2'), sg.Text('NÚMERO 3')],
    [sg.Input(key='number_1', size=13), sg.Input(key='number_2', size=13), sg.Input(key='number_3', size=13)],
    [sg.Text('ESCOLHA A OPERAÇÃO:')],
    [sg.Button(key='SOMAR', image_filename=foto_soma),
     sg.Button(key='MEDIA', image_filename=foto_media),
     sg.Button(key='CONCATENAR', image_filename=foto_concatenar)],
    [sg.Text(''), sg.Text(key='resultado'), sg.Button('LIMPAR')],
    [sg.Image(foto_gato, key='foto')]
]
janela_calculadora = sg.Window('CALCULADORA', layout=calculadora)
while True:
    evento, valor = janela_calculadora.read()
    if evento == sg.WIN_CLOSED:
        break
        janela_calculadora.close()
    elif evento == 'LIMPAR':
        limpar(janela_calculadora,valor)
    elif evento == 'SOMAR':
        soma(janela_calculadora, valor)
    elif evento == 'MEDIA':
        media(janela_calculadora, valor)
    elif evento == 'CONCATENAR':
        concatenar(janela_calculadora, valor)