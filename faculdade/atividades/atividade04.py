'''Crie um programa que peça ao usuário para inserir uma temperatura
e verifique se está frio, agradável ou quente'''

#1 passo: Irei receber o valor da temperatura
#2 passo: Definir os parametros para frio, agradavel e quente
#3 passo: Comparar os parametros com o valor que foi imformado
#4 passo: Informar o resultado para o usuario
#5 passo: Converter a temperatura do usuário

temperature = float(input('Insira a temperatura para saber como está o ambiente: '))
#condition = input('Você deseja alterar a escala de temperatura?\nDigite "1" para "SIM", ou "2" para "NÃO" alterar a escala: ')
#if condition == '1':
'''value = input('Qual a escala que você está fornecendo')
    convert = input('Em qual escala de temperatura você quer? ')'''
#else:
cold =  22
hot = 32
if temperature < cold:
    print('A temperatura está abaixo do normal, o tempo está frio!')
elif temperature > hot:
    print('A temperatura está acima do normal, o tempo está quente!')
else:
    print('A temperatura está dentro do normal, o tempo está agradável!')