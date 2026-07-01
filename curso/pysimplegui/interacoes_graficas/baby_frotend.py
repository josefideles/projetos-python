import PySimpleGUI
#pesquisar sobre lista em python
layout = [
    [PySimpleGUI.Text('USUÁRIO')],          #exibe o texto usuario
    [PySimpleGUI.Input(key='usuario')],     #recebe o nome do usuario
    [PySimpleGUI.Text('SENHA')],            #exibe o texto SENHA
    [PySimpleGUI.Input(key='senha', password_char='*')],       #recebe a senha do usuario, e a senha será digitada com o *
    [PySimpleGUI.Button('LOGAR')],         #criou um botao de logar
    [PySimpleGUI.Text('', key='validacao')] # cria uma mensagem em branco e recebe um valor para ser apresentado
]
layout_2 = [
    [PySimpleGUI.Text('PARABENS VOCÊ É UM USUÁRIO AUTORIZADO')],
    [PySimpleGUI.Text('SEJA BEM VINDO À NOSSA PÁGINA')]
]
janela = PySimpleGUI.Window('LOGUIN DO USUÁRIO', layout=layout)
entrada = PySimpleGUI.Window('PÁGINA INICIAL', layout=layout_2)
while True:
    evento, valor = janela.read()
    if evento == PySimpleGUI.WIN_CLOSED:
        break
    elif evento == 'LOGAR':
        usuario_correto = 'gabriel'
        senha_correta = 'fideles'
        usuario = valor['usuario']
        senha = valor['senha']
        if usuario == usuario_correto and senha == senha_correta:
            janela['validacao'].update('ACESSO AUTORIZADO')
            evento = entrada.read()
        else:
            janela['validacao'].update('ACESSO NEGADO')