'''Crie um programa que leia a altura e largura de uma parede 
e calcule a área dessa parede
e a quantidade de tinta (em litros) necessária para pintá-la 
sabendo que cada litro pinta uma área de 2m².
Depois apresente o catálogo da empresa "Vila dos Smurf's"
e forneça os valores e quantidades de latas que irá utilizar'''

import pandas as pd

print("Seja bem vindo à Vilda dos Smur'f tintaria\n")
      #'Para você saber quantos litros de tinta irá precisar, insira as informações a seguir:')

'''altura = float(input('Digite a altura do seu mural: '))
largura = float(input('Digite a largura do seu mural: '))
area = altura*largura
qtd_tinta = area/2'''

catalogo = pd.read_excel("catalogo.xlsx")
print(catalogo)

'''print('A área do seu mural é de', area, 'Metros quadrados')
print('Com 1L de tinta você consegue pintar 2 Metros quadrados. Para pintar o mural você irá precisar de:')
print(qtd_tinta, 'Litros de tinta.')'''