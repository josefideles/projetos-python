'''Crie um programa que leia um número em quilômetros 
e exiba na tela esse número convertido para metros e centímetros.'''

distancia = float(input('Digite a distância: '))

metro = distancia*1000
centimetro = distancia*100000

print('A sua distância é:', distancia, 'Km',
      '\n A distância em Metros é:', metro, 'M',
      '\n E a sua distância em Centímetros é:', centimetro, 'Cm')

# Refazer codigo com contatenacao
