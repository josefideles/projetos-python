'''Pegue as medidas do mural
Dizer a área e a quantidade de litos
Mostrar o catalogo
Dar opção de escolher o produto e para cada produto dar as informações:
Valor da tinta, qualidade e quantidade
Informar o preço e a quantidade para finalizar a compra'''

import pandas as pd
import openpyxl
import math
import time #time e diferente de times, sao duas bibliotecas diferentes
'''import pyautogui
pyautogui.PAUSE = (1)'''      #essa funcao ira demorar o tempo que for definido () para realizar cada código

welcome = ("\nSeja bem vindo à Vilda dos Smur'f tintaria\n\nPara você saber quantos litros de tinta irá precisar, insira as informações a seguir:")
print(welcome)

altura = float(input('Digite a altura do seu mural: '))
largura = float(input('Digite a largura do seu mural: '))
catalogo = pd.read_excel("catalogo.xlsx")
area = altura*largura
qtd_tinta = area/2
capacity_lata = 5
latas = math.ceil(qtd_tinta/capacity_lata)

'''if qtd_latas != qtd_tinta:
    latas = lata_int+1
else:
    latas = lata_int   

print('A área do seu mural é de', area, 'Metros quadrados')
print('Com 1L de tinta você consegue pintar 2 Metros quadrados. Para pintar o mural você irá precisar de:')
print(qtd_tinta, 'Litros de tinta.')'''

print('\n A área do seu mural é de {} Metros quadrados \n Com 1L de tinta você consegue pintar 2 Metros quadrados. \n Para pintar o mural você irá precisar de {} Litros de tinta!'.format(area, qtd_tinta))
time.sleep(5)     #ira pausar o codigo em 3 segundos
print('\n Irei te apresentar o catalogo de tintar para você escolher: \n\n{}'.format(catalogo))

tinta = (input('Qual a cor da tinta que você deseja?\nInsira o número da tinta que escolheu:'))

#ainda falta deixar a quantidade funcional. Tentar por aproximação
'''branco = 'branco', 'Branco'
cinza = 'cinza', 'Cinza'
laranja = 'laranja', 'Laranja'
azul = 'azul', 'Azul'
verde = 'verde', 'Verde'
preto = 'preto', 'Preto'''
valbranco = qtd_tinta*7
valcinza = qtd_tinta*7
vallaranja = qtd_tinta*10
valazul = qtd_tinta*11
valverde = qtd_tinta*11
valpreto = qtd_tinta*12

if tinta == 1:
    print('Você escolheu a cor branca e irá precisar de {} latas de tinta.\nE o valor será de {}'.format(latas, valbranco))
elif tinta == 2:
    print('Você escolheu a cor cinza e irá precisar de {} latas de tinta.\n E o valor será de {}'.format(latas, valcinza))
elif tinta == 3:
    print('Você escolheu a cor laranja e irá precisar de {} latas de tinta.\nE o valor será de {}'.format(latas, vallaranja))
elif tinta == 4:
    print('Você escolheu a cor azul e irá precisar de {} latas de tintas.\nE o valor será de {}'.format(latas, valazul))
elif tinta == 5:
    print('Você escolheu a cor verde e irá precisar de {} latas de tinta.\nE o valor será de {}'.format(latas, valverde))
elif tinta == 6:
    print('Você escolheu a cor preta e irá precisar de {} latas de tinta.\nE o valor será de {}'.format(latas, valpreto))
else:
    print('Não temos esse produto em nosso estoque')

'''print(latas)
print('Você irá precisar de {} latas de tintas para pinntar o seu mural'.format(qtd_latas))
if tinta == 1 or branco:
    print('Você escolheu a cor branca e irá precisar de {} latas de tinta.\nE o valor será de {}'.format(latas, valbranco))
elif tinta == 2 or cinza:
    print('Você escolheu a cor cinza e irá precisar de {} latas de tinta.\n E o valor será de {}'.format(latas, valcinza))
elif tinta == 3 or laranja:
    print('Você escolheu a cor laranja e irá precisar de {} latas de tinta.\nE o valor será de {}'.format(latas, vallaranja))
elif tinta == 4 or azul:
    print('Você escolheu a cor azul e irá precisar de {} latas de tintas.\nE o valor será de {}'.format(latas, valazul))
elif tinta == 5 or verde:
    print('Você escolheu a cor verde e irá precisar de {} latas de tinta.\nE o valor será de {}'.format(latas, valverde))
elif tinta == 6 or preto:
    print('Você escolheu a cor preta e irá precisar de {} latas de tinta.\nE o valor será de {}'.format(latas, valpreto))
else:
    print('Não temos esse produto em nosso estoque')'''
