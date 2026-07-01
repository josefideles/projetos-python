'''Crie um código que leia um número inteiro entre 1 e 7 
e esreva o dia da semana correspondente. 
Caso o usuário digite um número fora desse intervalo, 
deverá aparecer uma mensagem informando que não existe dia da semana com esse número'''
import pandas as pd

number = int(input('Insira um número inteiro entre 1 e 7 para saber o dia da semana: '))

semana = pd.DataFrame({
    'Number': [1, 2, 3, 4, 5, 6, 7],
    'Day': ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
})

#if number in semana['Number'].values:
    
'''if number == 1:
    print('Hoje é Domingo!! Descanse para ter um ótimo início de semana')
elif number == 2:
    print('Hoje é segunda-feira!! Tenha uma ótima semana')
elif number == 3:
    print('Hoje é terça-feira!! É o segundo dia da semana')
elif number == 4:
    print('Hoje é quarta-feira!! Estamos no meio da semana')
elif number == 5:
    print('Hoje é quinta-feira!! Estamos chegando perto do final de semana')
elif number == 6:
    print('Hoje é sexta-feira!! Já estamos com o pé no final de semana')
elif number == 7:
    print('Hoje é sábado!! Chegamos no final se semana. Partiu praia')
else:
    print('Acho que você bebeu demais nesse final de semana.\nNão temos esse dia da semana em nosso calendário!!')'''