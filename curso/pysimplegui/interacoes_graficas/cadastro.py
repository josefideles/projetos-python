#1 passo: Fazer uma tela de loguin para colocar o usuário e a senha
#2 passo: Criar a opção de entrar ou cadastrar usuário
#3 passo: Validar o usuário e abrir a tela do sistema
#4 passo: interagir na calculadora

import PySimpleGUI as pg

loguin = [
    [pg.Text('USUÁRIO')],
    [pg.Input(key='usuario')],
    [pg.Text('SENHA')],
    [pg.Input(key='senha')],
    [pg.Button('LOGAR'), pg.Button('NOVO CADASTRO')],
    [pg.Text('', key='mensagem')],
]
cadastro = [
    [pg.Text('Insira o seu nome:')],
    [pg.Input(key='nome')],
    [pg.Text('Insira o nome de usuário:')],
    [pg.Input(key='usuario_correto')],
    [pg.Text('Insira a sua senha:')],
    [pg.Input(key='senha_correta')],
    [pg.Button('CADASTRAR'), pg.Button('CANCELAR')],
]
janela_loguin = pg.Window('Loguin do Usuário', loguin)
janela_cadastro = pg.Window('Cadastro do Usuário', cadastro)
while True:
    evento, valor = janela_loguin.read()
    if evento == pg.WIN_CLOSED:
        break
    elif evento == 'NOVO CADASTRO':
            evento_cadastro, valor_cadastro = janela_cadastro.read()
            if evento_cadastro == pg.WIN_CLOSED or evento == 'CANCELAR':
                 janela_cadastro.close()
            elif evento_cadastro == 'CADASTRAR':
                nome = valor['nome']
                usuario_correto = valor['usuario_correto']
                senha_correta = valor['senha_correta']
                janela_cadastro.close()
    elif evento == 'LOGAR':
         mensagem = 'Você efetuou o loguin'
         valor['mensagem'].update(mensagem)
    
