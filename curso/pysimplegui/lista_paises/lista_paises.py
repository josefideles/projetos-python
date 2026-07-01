import PySimpleGUI as sg
#criar variaveis para as mensagens
mensagem_button = ''
mensagem_combo = ''
mensagem_radio = ''
mensagem_checkbox = 's'
#criar uma lista para o Checkbox
paises = ['AUSTRÁLIA', 'BRASIL', 'ITÁLIA']
exibir = []
janela = [
    [sg.Text('AUSTRÁLIA'), sg.Text('BRASIL'), sg.Text('ITÁLIA')],
    [sg.Button('australia'), sg.Button('brasil'), sg.Button('italia'), sg.Text('ESCOLHIDO:'), sg.Text(key='mensagem_button')],

    [sg.Text('Selecione um País:', background_color='red'),
     sg.Combo(paises, key='combo'), sg.Button('OK', key='ok_combo'),
     sg.Text('ESCOLHIDO:'), sg.Text(key='mensagem_combo')],

    [sg.Text('Selecione um País:', background_color='blue')],
    [sg.Radio('AUSTRÁLIA', 'FM', key='radio1'),
     sg.Radio('BRASIL', 'FM', key='radio2'),
     sg.Radio('ITÁLIA', 'FM', key='radio3'),
     sg.Button('OK', key='ok_radio'), sg.Text('ESCOLHIDO'), sg.Text(key='mensagem_radio')],

    [sg.Text('Selecione um País:', background_color='green')],
    [sg.Checkbox('AUSTRÁLIA', key='check1'), sg.Checkbox('BRASIL', key='check2'), sg.Checkbox('ITÁLIA', key='check3'),
     sg.Button('OK', key='ok_checkbox'), sg.Text('ESCOLHIDO(S):'), sg.Text('', key='mensagem_checkbox')],
]
janela_paises = sg.Window('LISTA PAÍSES', layout=janela, resizable=True)
#resizable=True, faz com que possamos diminuir o tamanho da janela, deixar em tela cheia
while True:
    event, values = janela_paises.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'australia':
        mensagem_button = janela_paises['mensagem_button'].update('AUSTRÁLIA')
    elif event == 'brasil':
        mensagem_button = janela_paises['mensagem_button'].update('BRASIL')
    elif event == 'italia':
        mensagem_button = janela_paises['mensagem_button'].update('ITÁLIA')


    elif event == 'ok_combo':
        mensagem_radio = janela_paises['mensagem_combo'].update(values['combo'])

    elif event == 'ok_radio':
        if values['radio1'] == True:
            janela_paises['mensagem_radio'].update('AUSTRÁLIA')
        if values['radio2'] == True:
            janela_paises['mensagem_radio'].update('BRASIL')
        if values['radio3'] == True:
            janela_paises['mensagem_radio'].update('ITÁLIA')

    elif event == 'ok_checkbox':
        if values['check1'] == True:
            exibir.append('AUSTRÁLIA') # .append e apenas para listas
            janela_paises['mensagem_checkbox'].update(exibir)
        if values['check2'] == True:
            exibir.append()
