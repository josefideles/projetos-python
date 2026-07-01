import PySimpleGUI as pg
calculadora = [
    [pg.Text('NÚMERO 1'), pg.Text('NÚMERO 2'), pg.Text('NÚMERO 3')],
    [pg.Input(key='number_1', size=13), pg.Input(key='number_2', size=13), pg.Input(key='number_3', size=13)],
    [pg.Text('ESCOLHA A OPERAÇÃO:')],
    [pg.Button('SOMAR'), pg.Button('MÉDIA'), pg.Button('CONCATENAR')],
    [pg.Text(''), pg.Text(key='resultado'), pg.Button('LIMPAR')],
    #[pg.Image(r"C:\Users\ALUNO\PycharmProjects\pythonProject\codigos\goku\pysimplegui\papai_smurf.png", size=(250,500))]
]
janela_calculadora = pg.Window('CALCULADORA', calculadora)
while True:
    evento, valor = janela_calculadora.read()
    if evento == pg.WINDOW_CLOSED:
        break
    number_1 = float(valor['number_1'])
    number_2 = float(valor['number_2'])
    number_3 = float(valor['number_3'])
    if evento == 'LIMPAR':
        janela_calculadora['number_1'].update('')
        janela_calculadora['number_2'].update('')
        janela_calculadora['number_3'].update('')
    elif evento == 'SOMAR':
        resultado = janela_calculadora['resultado'].update(f"O resultado é: {number_1+number_2+number_3}")
    elif evento == 'MÉDIA':
        resultado = janela_calculadora['resultado'].update(f"O resultado é: {(number_1 + number_2 + number_3)/3}")
    elif evento == 'CONCATENAR':
        resultado = janela_calculadora['resultado'].update(f"O resultado é: {valor['number_1']+valor['number_2']+valor['number_3']}")