import PySimpleGUI

layout = [
    [PySimpleGUI.Text('INSIRA A SUA NOTA:'), PySimpleGUI.Input(key='nota', size=10)],
    [PySimpleGUI.Text('A MÉDIA É DE 7 PONTOS!')],
    #[PySimpleGUI.Text('A SUA NOTA FOI DE: '), PySimpleGUI.Text('', key='resultado')],
    [PySimpleGUI.Button('CALCULAR')],
    [PySimpleGUI.Text('', key='mensagem')]
]

portal = PySimpleGUI.Window('PORTAL', layout=layout)

while True:
    evento, valor = portal.read()
    if evento == PySimpleGUI.WIN_CLOSED:
        break
    elif evento == 'CALCULAR':
        #resposta = portal['nota'].update(float(valor['nota']))
        #portal['resultado'].update(resposta)
        nota = float(valor['nota'])
        if nota < 7:
            portal['mensagem'].update('Infelizmente você foi reprovado, a sua nota foi inferior a média. Mas utilize essa nota como aprendizado para poder fechar a próxima prova.')
        elif nota > 10:
            portal['mensagem'].update('O limite da prova é de 10 pontos, e você não pode exceder a pontuação máxima para calcular a sua média!')
        else:
            portal['mensagem'].update('Ótimo! Você passou, a sua nota foi maior que a média.\nE o seu resultado vem de todo o seu esforço, continue assim!!!')
    else:
        portal['mensagem'].update('Não consegui realizar essa operação')