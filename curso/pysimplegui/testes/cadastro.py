import PySimpleGUI as pg
import time

loguin = [
    [pg.Text('USUÁRIO')],
    [pg.Input(key='usuario')],
    [pg.Text('SENHA')],
    [pg.Input(key='senha')],
    [pg.Button('LOGAR'), pg.Button('NOVO CADASTRO')],
    [pg.Text(''), pg.Text(key='validação')],
]
cadastro = [
    [pg.Text('NOME E SOBRENOME:')],
    [pg.Input(key='nome')],
    [pg.Text('NOME USUÁRIO:')],
    [pg.Input(key='nome_usuario')],
    [pg.Text('SENHA:')],
    [pg.Input(key='senha_usuario')],
    [pg.Text('E-MAIL:')],
    [pg.Input(key='email_usuario')],
    [pg.Button('CADASTRAR'), pg.Button('RETORNAR')],
    [pg.Text(''), pg.Text(key='mensagem')],
]
janela_loguin = pg.Window('LOGUIN', loguin)
janela_cadastro = pg.Window('CADASTRO', cadastro)
while True:
    evento, valor = janela_loguin.read()
    if evento == pg.WIN_CLOSED:
        break
    elif evento == 'LOGAR':
        if valor['usuario'] == usuario_correto and valor['senha'] == senha_correta:
            janela_loguin['mensagem'].update('USUÁRIO AUTORIZADO')
        elif evento == 'NOVO CADASTRO':
            evento_cadastro, valor_cadastro = janela_cadastro.read()
            if evento_cadastro == pg.WIN_CLOSED or evento_cadastro == 'CANCELAR':
                break
            elif evento_cadastro == 'CADASTRAR':
                if janela_cadastro['nome'] == '':
                    janela_cadastro['mensagem'].update('Dados inválidos')
                else:
                    usuario_correto = valor_cadastro['nome_usuario']
                    senha_correta = valor_cadastro['senha_usuario']
                    email_correto = valor_cadastro['email_usuario']
                    janela_cadastro['mensagem'].update('Usuário cadastrado')
                janela_cadastro['nome'].update('')
                janela_cadastro['nome_usuario'].update('')
                janela_cadastro['senha_usuario'].update('')
                janela_cadastro['email_usuario'].update('')
        else:
            janela_loguin['mensagem'].update('USUÁRIO OU SENHA INVÁLIDOS')
