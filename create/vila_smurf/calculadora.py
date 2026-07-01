'''faça a tabuada do número'''

#1 passo: pedir um núro para o usuário
#2 passo: fazer os cálculos
#3 passo: mostrar o resultado

number = int(input('Digite um número, natural e menor que 10, para saber a sua tabuada: '))
if number > 0 and number < 11:
    print('{} x {} = {}'.format(number, 1, number*1))
    print('{} x {} = {}'.format(number, 2, number*2))
    print('{} x {} = {}'.format(number, 3, number*3))
    print('{} x {} = {}'.format(number, 4, number*4))
    print('{} x {} = {}'.format(number, 5, number*5))
    print('{} x {} = {}'.format(number, 6, number*6))
    print('{} x {} = {}'.format(number, 7, number*7))
    print('{} x {} = {}'.format(number, 8, number*8))
    print('{} x {} = {}'.format(number, 9, number*9))
    print('{} x {} = {}'.format(number, 10, number*10))
else:
    print('Você já viu tabuada sem ser os números naturais, seu humano de conhecimento básico????????????????????????????')
    exit