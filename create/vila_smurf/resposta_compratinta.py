#Resposta do Python para o meu código

import pandas as pd
import math
import time

welcome = ("\nSeja bem-vindo à Vilda dos Smur'f tintaria\n\nPara você saber quantos litros de tinta irá precisar, insira as informações a seguir:")
print(welcome)

altura = float(input('Digite a altura do seu mural: '))
largura = float(input('Digite a largura do seu mural: '))
area = altura * largura
qtd_tinta = area / 2
capacity_lata = 5
latas = math.ceil(qtd_tinta / capacity_lata)
print('\n A área do seu mural é de {:.2f} Metros quadrados \n Com 1L de tinta você consegue pintar 2 Metros quadrados. \n Para pintar o mural você irá precisar de {:.2f} Litros de tinta!'.format(area, qtd_tinta))
time.sleep(7)  # irá pausar o código em 7 segundos

# Simulação de um catálogo fictício
catalogo = pd.DataFrame({
    'Número': [1, 2, 3, 4, 5, 6],
    'Cor': ['Branco', 'Cinza', 'Laranja', 'Azul', 'Verde', 'Preto'],
    'Valor por Litro': [7, 7, 10, 11, 11, 12]
})

print('\n Irei te apresentar o catálogo de tintas para você escolher:\n{}'.format(catalogo))

tinta = int(input('\nQual a cor da tinta que você deseja?\nInsira o número da tinta que escolheu: '))

# Verificando se a cor escolhida está no catálogo
if tinta in catalogo['Número'].values:
    cor_escolhida = catalogo.loc[catalogo['Número'] == tinta, 'Cor'].values[0]
    val_cor = qtd_tinta * catalogo.loc[catalogo['Número'] == tinta, 'Valor por Litro'].values[0]
    print('Você escolheu a cor {} e irá precisar de {} latas de tinta.\nE o valor será de {:.2f}'.format(cor_escolhida, latas, val_cor))
else:
    print('Não temos essa cor em nosso catálogo')