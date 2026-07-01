import PySimpleGUI as pg
import buttons
calculadora = [
    [pg.Text('NÚMERO 1'), pg.Text('NÚMERO 2'), pg.Text('NÚMERO 3')],
    [pg.Input(key='number_1', size=13), pg.Input(key='number_2', size=13), pg.Input(key='number_3', size=13)],
    [pg.Text('ESCOLHA A OPERAÇÃO:')],
    [pg.Button('', image_data=buttons.button_s_base64, key='SOMAR'),
     pg.Button('', image_data=buttons.button_m_base64, key='MÉDIA'),
     pg.Button('', image_data=buttons.button_c_base64, key='CONCATENAR')],
    [pg.Text(''), pg.Text(key='resultado'), pg.Button('LIMPAR')],
]
janela_calculadora = pg.Window('CALCULADORA', calculadora)  # grab_anywhere=True: Isso permite movimentar a janela de qualquer lugar
while True:
    evento, valor = janela_calculadora.read()
    if evento == pg.WINDOW_CLOSED:
        break
    valor_1 = valor['number_1']
    valor_2 = valor['number_2']
    valor_3 = valor['number_3']
    if evento == 'LIMPAR':
        janela_calculadora['number_1'].update('')
        janela_calculadora['number_2'].update('')
        janela_calculadora['number_3'].update('')
    elif evento == 'SOMAR' and valor['number_1'] != '':
        number_1 = float(valor['number_1'])
        number_2 = float(valor['number_2'])
        number_3 = float(valor['number_3'])
        resultado = janela_calculadora['resultado'].update(f"O resultado é: {number_1+number_2+number_3}")
        if valor == '':
            print('Esse é o valor:')
            print(valor)
        print(valor)
    elif evento == 'MÉDIA':
        number_1 = float(valor['number_1'])
        number_2 = float(valor['number_2'])
        number_3 = float(valor['number_3'])
        resultado = janela_calculadora['resultado'].update(f"O resultado é: {(number_1 + number_2 + number_3)/3}")
    elif evento == 'CONCATENAR':
        number_1 = float(valor['number_1'])
        number_2 = float(valor['number_2'])
        number_3 = float(valor['number_3'])
        resultado = janela_calculadora['resultado'].update(f"O resultado é: {valor['number_1']+valor['number_2']+valor['number_3']}")