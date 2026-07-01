import PySimpleGUI as bt

# declaração de variáveis de controle para exibir o resultado escolhido pelo usuário
mensagem_combo = " s"
mensagem_botao = " "
mensagem_radio = "a"
mensagem_check = "b"


# "paises" é uma lista de países que será exibida dentro do Combo
paises = ['AUSTRÁLIA', 'BRASIL', 'ITÁLIA']
# "exibir" é uma lista (inicialmente vazia) que vai receber e exibir os paises que o usuário escolher no Checkbox
exibir = []

#criação do layout visual da tela
visual = [
    [bt.Text('   AUSTRÁLIA               '), bt.Text('BRASIL               '), bt.Text('      ITÁLIA               ')],
    [bt.Button('australia'),
     bt.Text('     '),
     bt.Button('brasil'),
     bt.Text('     '),
     bt.Button('italia'),
     bt.Text('   ESCOLHIDO: '), bt.Text(key=mensagem_botao)],
    [bt.Text(180*'-')], # isso é para criar 180 tracinhos para dividir os espaços da tela
    [bt.Text('')],
    [bt.Text('Selecione um País: ', background_color='Brown'), bt.Combo(paises, font=('Times New Roman',16), size=12, key='lista_combo'), bt.Button('OK',size=9,key='ok_combo'), bt.Text('ESCOLHIDO: '), bt.Text(key=mensagem_combo)],
    [bt.Text('')],
    [bt.Text(180*'-')],
    [bt.Text('')],
    [bt.Text('Selecione um País: ', background_color='DarkBlue')], # o método "background_color" insere uma cor no fundo da fonte
    [bt.Radio('AUSTRÁLIA  ','grupo',key='radio1'), bt.Radio('BRASIL  ','grupo',key='radio2'), bt.Radio('ITÁLIA  ','grupo',key='radio3'), bt.Button('OK', size=9, key='ok_radio'), bt.Text('ESCOLHIDO: '), bt.Text(key=mensagem_radio)],
    [bt.Text('')],# lembrar de sempre colocar as alternativas do "Radio" sempre no mesmo grupo para evitar de selecionar mais de uma opção
    [bt.Text(180 * '-')],
    [bt.Text('Selecione um País: ', background_color='Green')],
    [bt.Checkbox('AUSTRÁLIA  ',key='check1'), bt.Checkbox('BRASIL  ', key='check2'), bt.Checkbox('ITÁLIA  ', key='check3'), bt.Button('OK', key='ok_check', size=9), bt.Text('ESCOLHIDO(S): '), bt.Text(key=mensagem_check)],
    [bt.Text('')],
    [bt.Text(180 * '-')],

]

tela = bt.Window('lista de países'.upper(), layout=visual, size=(730,600), resizable=True, grab_anywhere=True)
# o método ".upper()" é para deixar uma string em MAIÚSCULA
while True:
    evento, valor = tela.read()

    if evento == bt.WINDOW_CLOSED:
        break
    elif evento == 'australia':
        tela[mensagem_botao].update('AUSTRÁLIA')
    elif evento == 'brasil':
        tela[mensagem_botao].update('BRASIL')
    elif evento == 'italia':
        tela[mensagem_botao].update('ITÁLIA')
# o trecho acima é para verificar qual botão foi apertado e atualizar o valor de "mensagem_botao"



    elif evento == 'ok_combo':
        tela[mensagem_combo].update(valor['lista_combo'])
# o trecho acima é para "pegar" e atualizar o valor escolhido pelo usuário no Combo no "mensagem_combo



    elif evento == 'ok_check':
        exibir.clear()
        if valor['check1'] == True:
            exibir.append('AUSTRÁLIA')
            tela[mensagem_check].update(exibir)
        elif valor['check2'] == True:
            exibir.append('BRASIL')
            tela[mensagem_check].update(exibir)
        elif valor['check3'] == True:
            exibir.append('ITÁLIA')
            tela[mensagem_check].update(exibir)

# O trecho acima é para verificar quantas "caixinhas de Check" o usuário marcou e atualizar o "mensagem_check"



    if evento == 'ok_radio':
        if valor['radio1'] == True:
            tela[mensagem_radio].update('AUSTRÁLIA')
        if valor['radio2'] == True:
            tela[mensagem_radio].update('BRASIL')
        if valor['radio3'] == True:
            tela[mensagem_radio].update('ITÁLIA')
# o trecho acima é para verificar qual foi o "radio" escolhido pelo usuário e atualizar o valor de mensagem_radio
# lembrando que nesse modelo só pode escolher uma entre todas as opções da tela.