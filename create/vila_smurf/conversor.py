'''Criar um programa que aceite um valor
e dê a opção de escolher qual moeda é esse valor
e converter para outro valor que a pessoa deseja'''

import pandas as pd

number = float(input('Digite um valor para convertê-lo para outras moedas: '))

moedas = pd.DataFrame({
    'Moedas': ['Real', 'Dolar', 'Euro', 'Peso'],
    'País': ['Brasil', 'EUA', 'Espanha', 'Argentina'],
    'Valores': [1, 4.97, 5.36, 73.80]
})

print('O seu valor foi {}.\nEssa é a nossa "Tabela de conversão": '.format(number))
print(moedas)

moeda_number = input('Para qual moeda você deseja converter? Escolha uma moeda dentro da "Tabela de conversão": ')

if moeda_number in moedas['Moedas'].values:
    pais_ecolhido = moedas.loc[moedas['Moedas'] == moeda_number, 'País'].values[0]
    valor_convertido = number * moedas.loc[moedas['Moedas'] == moeda_number, 'Valores'].values[0]
    print('Você escolheu a moeda {} do país de {}.\nE o seu valor de {} convertido para {} será no valor de {}'
          .format(moeda_number, pais_ecolhido, number, moeda_number, valor_convertido))